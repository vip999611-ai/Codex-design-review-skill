#!/usr/bin/env python3

import sys
import unittest
from pathlib import Path


SKILL_SCRIPTS = Path(__file__).resolve().parents[1] / "design-review" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))

from validate_score import ScoreError, calculate  # noqa: E402


def dimensions(scores=None):
    values = scores or [8, 8, 8, 8]
    return [
        {"name": "goal", "weight": 25, "score": values[0]},
        {"name": "hierarchy", "weight": 25, "score": values[1]},
        {"name": "craft", "weight": 25, "score": values[2]},
        {"name": "delivery", "weight": 25, "score": values[3]},
    ]


class ValidateScoreTests(unittest.TestCase):
    def test_normal_score(self):
        result = calculate({"route": "poster", "dimensions": dimensions(), "confidence": "high"})
        self.assertEqual(result["final_score"], 80)
        self.assertFalse(result["renormalized"])
        self.assertEqual(result["rating"], "strong / minor-to-moderate refinement")

    def test_na_renormalizes_supported_weights(self):
        result = calculate(
            {"route": "ppt", "dimensions": dimensions([8, 8, 8, None]), "provisional": True}
        )
        self.assertEqual(result["supported_weight"], 75.0)
        self.assertTrue(result["renormalized"])
        self.assertEqual(result["final_score"], 80)
        self.assertEqual(result["status"], "provisional expert score")

    def test_s0_cap(self):
        result = calculate({"route": "data", "dimensions": dimensions([10, 10, 10, 10]), "unresolved_s0": True})
        self.assertEqual(result["raw_total"], 100.0)
        self.assertEqual(result["final_score"], 59)

    def test_essential_failure_cap_beats_s0_cap(self):
        result = calculate(
            {
                "route": "data",
                "dimensions": dimensions([10, 10, 10, 10]),
                "unresolved_s0": True,
                "essential_failure": True,
            }
        )
        self.assertEqual(result["final_score"], 49)

    def test_rejects_invalid_weight_total(self):
        bad = dimensions()
        bad[0]["weight"] = 20
        with self.assertRaisesRegex(ScoreError, "weights must total 100"):
            calculate({"route": "brand", "dimensions": bad})

    def test_rejects_score_out_of_range(self):
        with self.assertRaisesRegex(ScoreError, "between 0 and 10"):
            calculate({"route": "brand", "dimensions": dimensions([11, 8, 8, 8])})

    def test_rejects_numeric_score_from_too_little_evidence(self):
        with self.assertRaisesRegex(ScoreError, "at least 50"):
            calculate({"route": "ppt", "dimensions": dimensions([8, None, None, None])})

    def test_rejects_unreasoned_manual_adjustment(self):
        with self.assertRaisesRegex(ScoreError, "reason is required"):
            calculate(
                {"route": "ui", "dimensions": dimensions(), "manual_adjustment": {"points": 2}}
            )

    def test_reasoned_manual_adjustment_is_explicit(self):
        result = calculate(
            {
                "route": "mixed",
                "dimensions": dimensions(),
                "manual_adjustment": {"points": -2, "reason": "Declared route-specific risk"},
            }
        )
        self.assertEqual(result["final_score"], 78)
        self.assertEqual(result["manual_adjustment"]["reason"], "Declared route-specific risk")

    def test_rounds_half_up(self):
        result = calculate({"route": "poster", "dimensions": dimensions([8.05, 8.05, 8.05, 8.05])})
        self.assertEqual(result["final_score"], 81)


if __name__ == "__main__":
    unittest.main()
