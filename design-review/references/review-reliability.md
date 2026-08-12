# Review reliability and evidence boundaries

Apply this module to every review.

## Distinguish the method

### Visual design critique

Use for concept, expression, visual language, form, cultural/contextual meaning, and craft. Ground the argument in visible evidence and the design contract. Accept that more than one defensible solution can exist.

### Expert heuristic review

Use to identify potential problems by comparing the artifact with project rules, applicable standards, design systems, professional principles, and prior research knowledge. Treat findings as expert inspection, not proof of user behavior.

### User testing

Require representative users performing realistic tasks or responding in the intended viewing context. Recommend user testing when the question is whether people notice, understand, prefer, trust, remember, convert, or complete a task. Never write "users will" or "users cannot" when no user evidence exists; write "may", "risk", or "test whether".

Expert review can find plausible issues quickly. It cannot validate audience preference, conversion lift, brand recall, emotional response, task success, or real-world accessibility by itself.

## Evidence taxonomy

Label findings with one primary evidence type:

- **Direct observation:** visibly present in the supplied artifact, such as competing focal points, clipped text, or a misleading axis.
- **Guideline-backed:** supported by an applicable A/B-level requirement or professional guideline.
- **Professional inference:** likely effect derived from visible relationships and domain expertise; state assumptions.
- **Needs verification:** source file, project rule, production proof, analytics, or user research is required.

Use source levels:

- **A — governing/official:** applicable laws/regulations and non-waivable mandatory accessibility/safety requirements; project and brand specifications supplied by the user; platform-owner requirements.
- **B — institutional/professional:** mature design systems, professional bodies, established research/education sources.
- **C — practitioner heuristic:** tutorials, practitioner articles, case analyses, and reviewer experience.

Rules:

- Do not elevate C-level advice into a universal rule.
- Do not create S0/S1 solely from C-level guidance.
- Allow direct observation to support S1 when the failed design goal is explicit and visible.
- Cite the nearest source for an A-level or high-risk claim.
- When sources conflict, apply: applicable law/regulation and non-waivable mandatory requirement > user project/brand rule > applicable platform/medium requirement > professional principle > practitioner technique. If a project rule conflicts with a mandatory requirement, flag it for correction.

## Independent panel protocol

Before synthesis, each relevant lens records independently:

1. The single most important strength to preserve
2. Up to three root problems
3. The highest severity justified by its evidence
4. What cannot be known

Then synthesize:

- Merge duplicate symptoms under one root cause.
- Reject a finding that only restates preference without a goal, observable impact, or credible principle.
- Preserve dissent when goals conflict, for example brand expressiveness versus conservative legibility.
- Explain the condition that changes the recommendation instead of forcing consensus.
- Do not show fabricated panel vote counts; these are analytical lenses, not real people.

## Bias controls

- **Authority bias:** a senior/creative lens does not override measured or governing evidence.
- **Groupthink:** collect observations independently before synthesis.
- **First-idea anchoring:** inspect full view, thumbnail, detail, and alternate interpretations before locking the diagnosis.
- **Minimalism bias:** density is not a defect when hierarchy and task support remain strong.
- **Trend/familiarity bias:** unfamiliar or unfashionable work is not automatically weak.
- **Style cloning:** do not recommend making every artifact resemble current award-gallery aesthetics.
- **Halo effect:** strong imagery does not excuse wrong data, weak content, or inaccessible essentials.
- **Precision bias:** exact-looking numbers are not more valid when the source is a screenshot.

## Confidence and provisional scores

Assign confidence to the report and individual findings:

- **High:** clear direct evidence plus a known design contract or applicable source properties.
- **Medium:** artifact is clear but some context, rules, or source properties are missing.
- **Low:** artifact is partial, compressed, ambiguous, or shown outside the real viewing context.

Mark the score **provisional** when any essential design-contract field is assumed, the artifact is incomplete, or source-only properties could materially change the outcome. Do not score unseen behavior or properties; mark them N/A and renormalize supported weights.

Do not produce a numeric score when supported dimensions retain fewer than 50 of the original 100 weight points, the primary message/subject cannot be identified at all, or image quality prevents reliable separation of major elements. Write `无法可靠评分`, request the minimum clearer artifact/context, and report only high-confidence direct observations. This threshold prevents a precise-looking total from a tiny evidence base.

## Escalation beyond expert review

Recommend the smallest valid next check:

- User comprehension/attention: 5-second or first-click test with representative viewers
- Preference or emotional fit: structured comparison with target-audience participants
- Usability/task success: moderated or unmoderated task test
- Accessibility: source inspection plus automated checker and assistive-technology/manual testing
- Brand compliance: compare against the approved brand guide and asset package
- Print fitness: preflight plus physical proof under intended stock, process, and lighting
- Data truth: verify source data, transformations, definitions, and chart encoding

## Reliability check before publishing

- Every S0/S1 has an evidence type.
- No S0/S1 rests only on a C-level source.
- No statement converts inference into observed user behavior.
- Missing dimensions are N/A, not guessed.
- Recommendations preserve at least one intentional strength.
- A reviewer disagreement is retained when the tradeoff is real.
- Score arithmetic and caps are validated.
