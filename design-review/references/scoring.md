# Scoring model

Use a 100-point weighted score only after written diagnosis. Score the artifact against its design contract, not against a universal style. A score represents expert assessment of visible/supported dimensions; it does not represent tested usability, preference, conversion, or market performance.

## Dimension anchors

Score each supported dimension from 0 to 10:

- 9–10: exceptional, coherent, production-ready; issues are minor polish
- 7–8: strong and effective; several meaningful refinements remain
- 5–6: workable but visibly uneven; important issues reduce quality or clarity
- 3–4: weak; multiple high-impact problems obstruct the goal
- 1–2: fundamentally ineffective or misleading
- 0: absent, broken, or impossible to evaluate because the artifact itself fails the essential requirement

Use `N/A` rather than guessing. Renormalize weights across supported dimensions and disclose this. Do not compensate for an unseen dimension by subjectively raising or lowering another dimension.

If positive-weight supported dimensions total less than 50, do not calculate or report a numeric score. Request a clearer/more complete artifact or the missing source evidence. The script rejects this condition.

## Default route weights

| Dimension | Poster/banner | Brand | IP/character | PPT | Data viz | UI |
|---|---:|---:|---:|---:|---:|---:|
| Goal/message effectiveness | 20 | 15 | 10 | 20 | 15 | 20 |
| Concept/brand/character fit | 15 | 25 | 30 | 10 | 5 | 5 |
| Hierarchy/composition/narrative | 20 | 15 | 15 | 20 | 15 | 15 |
| Typography/content clarity | 15 | 10 | 5 | 15 | 10 | 15 |
| Color/image/icon craft | 15 | 15 | 20 | 10 | 10 | 10 |
| System consistency/repeatability | 5 | 15 | 15 | 10 | 10 | 15 |
| Accessibility/delivery fitness | 10 | 5 | 5 | 15 | 15 | 20 |
| Data truth/decision support | 0 | 0 | 0 | 0 | 20 | 0 |
| **Total** | **100** | **100** | **100** | **100** | **100** | **100** |

For mixed work, select the dominant route and adjust at most 15 weight points. State adjustments.

## Calculation

For each dimension: `dimension score / 10 × weight`. Display or internally record every weighted contribution, sum the unrounded contributions, then round the final sum to the nearest whole number. Verify the arithmetic once before publishing. If the reported total differs because of a cap or declared weight adjustment, show the raw total and the applied adjustment; never silently nudge a score to match a qualitative label.

Prefer `scripts/validate_score.py` for calculation. Pass N/A dimensions as `null`; the script renormalizes only across supported positive-weight dimensions.

## Quality gates and caps

Apply caps after the weighted score:

- Any unresolved S0: total cannot exceed 59.
- Essential message/data demonstrably wrong or unreadable: total cannot exceed 49.
- Missing context alone does not cap the score; lower confidence and mark dimensions N/A.
- A likely but unmeasured contrast risk does not trigger a cap unless essential content is visibly unreadable in the supplied use context.

## Rating labels

- 90–100: exceptional / ready with polish
- 80–89: strong / minor-to-moderate refinement
- 70–79: solid direction / meaningful refinement needed
- 60–69: workable / substantial revision needed
- Below 60: major rework required

Always pair the score with confidence:

- High: clear artifact plus goal/channel/spec or source properties
- Medium: clear artifact but some context/source information missing
- Low: partial, compressed, ambiguous, or wrong viewing context

Also mark status:

- **Final expert score:** essential contract and scored source properties are known.
- **Provisional expert score:** essential context is assumed, the artifact is partial/compressed, or source-only properties could materially change the result.

Never imply that a 1-point difference is meaningful. For comparisons, treat differences under 3 points as effectively tied unless a decisive goal-specific issue separates them.
