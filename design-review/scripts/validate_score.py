#!/usr/bin/env python3
"""Validate and calculate Design Review Skill scores from a JSON document.

The script uses only the Python standard library. Read JSON from --input or stdin
and write deterministic JSON to stdout. Errors go to stderr with exit code 2.
"""

from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


ROUTES = {
    "poster": "poster/banner",
    "banner": "poster/banner",
    "poster/banner": "poster/banner",
    "brand": "brand",
    "ip": "ip/character",
    "character": "ip/character",
    "ip/character": "ip/character",
    "ppt": "ppt",
    "presentation": "ppt",
    "data": "data-viz",
    "data-viz": "data-viz",
    "data_visualization": "data-viz",
    "ui": "ui",
    "mixed": "mixed",
}

LABELS = (
    (90, "exceptional / ready with polish"),
    (80, "strong / minor-to-moderate refinement"),
    (70, "solid direction / meaningful refinement needed"),
    (60, "workable / substantial revision needed"),
    (0, "major rework required"),
)


class ScoreError(ValueError):
    pass


def decimal_value(value: Any, field: str) -> Decimal:
    if isinstance(value, bool):
        raise ScoreError(f"{field} must be numeric, not boolean")
    try:
        number = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ScoreError(f"{field} must be numeric") from exc
    if not number.is_finite():
        raise ScoreError(f"{field} must be finite")
    return number


def rounded_int(value: Decimal) -> int:
    return int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def display_decimal(value: Decimal) -> float:
    return float(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def rating_label(score: int) -> str:
    for minimum, label in LABELS:
        if score >= minimum:
            return label
    raise AssertionError("unreachable")


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ScoreError("input must be a JSON object")

    route_input = str(payload.get("route", "")).strip().lower()
    if route_input not in ROUTES:
        raise ScoreError(f"unsupported route: {route_input or '<missing>'}")
    route = ROUTES[route_input]

    dimensions = payload.get("dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        raise ScoreError("dimensions must be a non-empty array")

    seen_names: set[str] = set()
    total_weight = Decimal("0")
    supported_weight = Decimal("0")
    raw_contribution = Decimal("0")
    parsed: list[dict[str, Any]] = []

    for index, dimension in enumerate(dimensions):
        prefix = f"dimensions[{index}]"
        if not isinstance(dimension, dict):
            raise ScoreError(f"{prefix} must be an object")
        name = str(dimension.get("name", "")).strip()
        if not name:
            raise ScoreError(f"{prefix}.name is required")
        if name in seen_names:
            raise ScoreError(f"duplicate dimension name: {name}")
        seen_names.add(name)

        weight = decimal_value(dimension.get("weight"), f"{prefix}.weight")
        if weight < 0 or weight > 100:
            raise ScoreError(f"{prefix}.weight must be between 0 and 100")
        total_weight += weight

        score_input = dimension.get("score")
        if score_input is None:
            parsed.append(
                {"name": name, "weight": display_decimal(weight), "score": None, "weighted_points": None}
            )
            continue

        score = decimal_value(score_input, f"{prefix}.score")
        if score < 0 or score > 10:
            raise ScoreError(f"{prefix}.score must be between 0 and 10 or null")
        if weight > 0:
            supported_weight += weight
            contribution = score / Decimal("10") * weight
            raw_contribution += contribution
        else:
            contribution = Decimal("0")
        parsed.append(
            {
                "name": name,
                "weight": display_decimal(weight),
                "score": display_decimal(score),
                "weighted_points_before_renormalization": display_decimal(contribution),
            }
        )

    if total_weight != Decimal("100"):
        raise ScoreError(f"dimension weights must total 100; got {total_weight}")
    if supported_weight <= 0:
        raise ScoreError("at least one positive-weight dimension must have a score")
    if supported_weight < Decimal("50"):
        raise ScoreError(
            f"supported positive weight must be at least 50 to report a numeric score; got {supported_weight}"
        )

    renormalization_factor = Decimal("100") / supported_weight
    for dimension in parsed:
        if dimension["score"] is None:
            continue
        contribution = (
            Decimal(str(dimension["score"]))
            / Decimal("10")
            * Decimal(str(dimension["weight"]))
            * renormalization_factor
        )
        dimension["weighted_points"] = display_decimal(contribution)

    raw_total = raw_contribution * renormalization_factor

    adjustment = payload.get("manual_adjustment")
    adjustment_points = Decimal("0")
    adjustment_reason = None
    if adjustment is not None:
        if not isinstance(adjustment, dict):
            raise ScoreError("manual_adjustment must be an object")
        adjustment_reason = str(adjustment.get("reason", "")).strip()
        if not adjustment_reason:
            raise ScoreError("manual_adjustment.reason is required")
        adjustment_points = decimal_value(adjustment.get("points"), "manual_adjustment.points")
        if adjustment_points < -15 or adjustment_points > 15:
            raise ScoreError("manual_adjustment.points must be between -15 and 15")

    adjusted_total = max(Decimal("0"), min(Decimal("100"), raw_total + adjustment_points))

    unresolved_s0 = bool(payload.get("unresolved_s0", False))
    essential_failure = bool(payload.get("essential_failure", False))
    unresolved_s1 = int(payload.get("unresolved_s1", 0))
    if unresolved_s1 < 0:
        raise ScoreError("unresolved_s1 must be zero or greater")

    caps: list[dict[str, Any]] = []
    cap = Decimal("100")
    if unresolved_s0:
        cap = min(cap, Decimal("59"))
        caps.append({"maximum": 59, "reason": "unresolved S0"})
    if essential_failure:
        cap = min(cap, Decimal("49"))
        caps.append({"maximum": 49, "reason": "essential message/data wrong or unreadable"})

    final_decimal = min(adjusted_total, cap)
    final_score = rounded_int(final_decimal)

    provisional = bool(payload.get("provisional", False))
    confidence = str(payload.get("confidence", "medium")).strip().lower()
    if confidence not in {"high", "medium", "low"}:
        raise ScoreError("confidence must be high, medium, or low")

    result: dict[str, Any] = {
        "route": route,
        "status": "provisional expert score" if provisional else "final expert score",
        "confidence": confidence,
        "dimensions": parsed,
        "weights_total": 100,
        "supported_weight": display_decimal(supported_weight),
        "renormalized": supported_weight != Decimal("100"),
        "renormalization_factor": display_decimal(renormalization_factor),
        "raw_total": display_decimal(raw_total),
        "adjusted_total": display_decimal(adjusted_total),
        "caps": caps,
        "final_score": final_score,
        "rating": rating_label(final_score),
        "unresolved_s0": unresolved_s0,
        "unresolved_s1": unresolved_s1,
        "essential_failure": essential_failure,
    }
    if adjustment is not None:
        result["manual_adjustment"] = {
            "points": display_decimal(adjustment_points),
            "reason": adjustment_reason,
        }
    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON input file; omit to read stdin")
    parser.add_argument("--pretty", action="store_true", help="pretty-print JSON output")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.input:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
        else:
            payload = json.load(sys.stdin)
        result = calculate(payload)
    except (OSError, json.JSONDecodeError, ScoreError, ValueError) as exc:
        print(f"score validation error: {exc}", file=sys.stderr)
        return 2

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2 if args.pretty else None)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
