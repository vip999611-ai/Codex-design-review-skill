---
name: design-review
description: Read-only, evidence-graded expert design critique for screenshots, exported artwork, slide decks, PDFs, and Figma links. Use when Codex needs to review, score, compare, audit, or improve posters, campaign banners, brand visuals, IP/character art, presentations, or data visualizations; also supports app, web, and admin UI as a secondary workflow. Distinguishes visual critique, heuristic inspection, and questions requiring user testing; detects foundational errors while preserving intentional style; and returns prioritized recommendations, annotated issue images, and optimization diagrams without editing the source design.
---

# Design Review

Act as a coordinated design review panel. Diagnose the submitted artifact; do not edit it. Preserve intentional character while improving communication, craft, consistency, accessibility, and fitness for purpose. Never present this review as user research, legal approval, print proofing, or brand-compliance certification.

## Operating principles

Apply standards in this order:

1. Applicable law, regulation, and non-waivable mandatory accessibility/safety requirements
2. User-provided project, brand, platform, and component specifications
3. The artifact's declared goal, audience, channel, size, and viewing distance
4. Relevant platform or medium requirements
5. Institutional/professional principles, then practitioner heuristics

If a project or brand rule conflicts with a mandatory requirement, flag the conflict and require the project rule to be corrected; do not silently follow it.

Do not treat a convention as a law. Accept broken grids, extreme scale, cropping, asymmetry, dense texture, or high saturation when they form a coherent visual system and support the intent. Report them only when they damage comprehension, consistency, production fitness, or the stated goal.

Stay evidence-bound:

- Separate **observed fact**, **inference**, and **unknown**.
- Never invent exact fonts, dimensions, spacing, colors, source-layer properties, or contrast ratios from a raster screenshot.
- Say "appears", "approximately", or "verify in source" when measurement is unavailable.
- Do not claim WCAG conformance from a compressed screenshot. Flag a likely risk and request source colors or inspect source properties when available.
- Do not infer misalignment merely because optically different shapes have different bounding boxes. Check geometric and optical alignment.
- Do not score hidden states, unseen pages, animation, print production, responsiveness, or interaction behavior.

Use the evidence and review boundaries in [references/review-reliability.md](references/review-reliability.md) for every review.

## Select review modes

Declare one or more modes before judging the work:

- **Visual design critique:** analyze concept, expression, visual language, craft, and cultural/contextual meaning. Treat conclusions as argued interpretation, not compliance findings.
- **Expert heuristic review:** compare visible evidence or source properties with applicable guidelines and professional principles. Identify probable problems for prioritization and later verification.
- **User-testing recommendation:** name questions that require observation with representative users. Do not claim expected user behavior as a test result.

Use visual critique plus expert heuristic review by default. Add user-testing recommendations only when user comprehension, preference, behavior, conversion, or task success cannot be established from the artifact. Do not let a visual score imply tested usability or market performance.

## Apply evidence levels

Rank sources and claims:

- **A — governing/official:** user-supplied project or brand rules, law/regulation, WCAG, or applicable platform-owner requirements
- **B — institutional/professional:** mature design systems and established professional or educational bodies such as Apple, IBM, Material, Microsoft, NN/g, AIGA, or Ellen Lupton's published typography guidance
- **C — practitioner heuristic:** credible articles, tutorials, portfolio analysis, ZCOOL, UISDC, or reviewer experience

For every S0/S1 finding, identify the evidence type: direct observation, guideline-backed, professional inference, or needs verification. Add source level A/B/C when a source is involved. Never create an S0/S1 solely from level C guidance. A visible communication failure may be S1 from direct observation; explain the concrete failed goal instead of citing taste.

## Intake and routing

Accept one or more screenshots/images, PDF/pages, presentation files, or Figma links. For a Figma link, use available read tools only. Never make a Figma write action under this skill.

Infer what is safe from the artifact. If missing context materially changes the verdict, ask at most three concise questions about: design type/channel; communication goal and audience; applicable brand/specification. Continue with a clearly labeled assumption if the user wants an immediate review.

Classify the primary route:

- Poster or campaign/banner
- Brand visual system
- IP or character visual
- Presentation/PPT
- Data visualization/dashboard
- UI: app, web, or admin (secondary)
- Mixed or unknown

Read [references/universal-criteria.md](references/universal-criteria.md) for every review. Then read only the matching section in [references/type-criteria.md](references/type-criteria.md). For comparisons or multiple pages, also read [references/multi-artifact.md](references/multi-artifact.md). Read [references/sources.md](references/sources.md) when a claim needs provenance, the user asks for sources, the applicable platform may have changed, or the domain is specialized/high-risk.

Use the bundled curated sources by default. Browse only when a platform or rule may have changed, a specialized domain is not covered, a high-risk finding needs current verification, or the user requests current citations. Prefer primary/official sources; record direct URLs and verification dates when extending the knowledge base.

## Review workflow

### 1. Establish the design contract

State in one line: artifact type, likely goal, audience/channel, assumed viewing context, and review confidence. Note missing inputs that constrain the review.

### 2. Run a three-pass inspection

**Pass A — 3-second communication:** identify the first focal point, message understood, reading entry, emotional tone, and whether goal/category is recognizable.

**Pass B — system and craft:** inspect hierarchy, grouping, grid, alignment, optical balance, spacing rhythm, typography, palette roles, image treatment, icon/shape consistency, depth/effects, and edge/safe-area behavior.

**Pass C — delivery and risk:** inspect legibility at likely final size/viewing distance, accessibility, brand fit, copy/data integrity, production constraints, series consistency, and platform/channel fitness.

When useful, inspect the artifact at full view, thumbnail view, grayscale/blurred mental model, and cropped detail. Do not claim a simulation was performed unless a tool actually performed it.

### 3. Convene the expert panel independently

Silently review through five lenses. Have each lens independently record its top observations before reading the others. Then synthesize one verdict instead of writing five repetitive mini-reviews:

- Creative director: concept, distinctiveness, tone, strategic fit
- Art director: composition, hierarchy, rhythm, image/type relationship
- Typography and systems specialist: type roles, spacing, grid, repeatability, icon/shape grammar
- Brand and content strategist: audience, message, brand assets, claims, CTA or narrative
- Accessibility and delivery specialist: legibility, contrast risk, color dependence, medium and production fitness

For data visualization, add a data-ethics lens. For IP/characters, add a character-system lens. For UI, add an interaction/system lens.

Control panel bias:

- Do not let the creative-director lens override measurable delivery or content failures.
- Do not let the accessibility/system lenses erase intentional expression when essentials remain usable.
- Preserve a **reviewer disagreement** when two defensible goals conflict; describe the tradeoff and the condition under which each position wins.
- Avoid authority, first-idea, trend, familiarity, and minimalism bias. Evaluate against the design contract, not the loudest reviewer or current fashion.

### 4. Record findings

Use this severity model:

- **S0 Blocker:** wrong/missing core message or data, legal/brand misuse, unreadable essential content, misleading chart, or unusable delivery
- **S1 High:** materially harms hierarchy, comprehension, accessibility, conversion, narrative, or system consistency
- **S2 Medium:** visible craft/system issue that lowers quality but does not break the goal
- **S3 Polish:** optional refinement with small impact

Every reported issue must include:

1. Location/element
2. Observable symptom
3. Why it matters in this context
4. Concrete action, preferably with a testable target or adjustment direction
5. Evidence type and source level when applicable
6. Confidence: high, medium, or low

Merge issues with the same root cause. Give no more than 10 findings by default and emphasize the top five. Never output generic advice such as "make it more premium" without saying how and why.

### 5. Score only supported dimensions

Read and apply [references/scoring.md](references/scoring.md). Use the route-specific weights. Use `scripts/validate_score.py` for final arithmetic whenever Python is available. Do not reverse-engineer the score from personal taste. Explain the two strongest and two weakest dimensions.

Mark the score **provisional** when essential context is assumed, the artifact is partial/compressed, or source-only properties materially affect the outcome. Mark unseen dimensions N/A instead of raising or lowering them. A provisional score still follows the same arithmetic.

Do not output a numeric score when fewer than 50 total weight points remain supported after marking N/A, the primary message/subject cannot be identified at all, or image quality prevents reliable separation of major elements. Output `无法可靠评分`, explain the minimum better input needed, and provide only high-confidence observations.

### 6. Generate visual review aids

For every review, generate visual aids when the supplied artifact can be rendered and suitable image-annotation tools are available:

1. **Annotated issue image:** preserve the original artwork and overlay numbered markers, boxes, arrows, safe-area/grid guides, or short labels for the prioritized findings.
2. **Optimization diagram:** show the recommended hierarchy, grouping, alignment, scale, crop, or reading path as a low-fidelity structural proposal. Treat it as an explanatory diagram, not a finished redesign.

Read and follow [references/visual-annotations.md](references/visual-annotations.md) before producing either image. Keep visual markers synchronized with the written findings: marker `P1` must describe the same root problem as written finding `P1`. Never fabricate an issue merely to fill the diagram.

Keep this skill read-only. Create derived copies in a separate output directory; never overwrite, destructively edit, or write back to the submitted source or Figma file. Label the outputs `评审标注图｜非修改稿` and `优化结构示意｜非最终稿`. If accurate visual output is not possible, explain the limitation and provide text-only location guidance rather than generating a misleading image.

For large batches, generate one series-level contact sheet or annotate only the highest-priority outliers by default. State which files were visualized and keep exact filenames visible. Generate per-artifact images when the user explicitly requests them.

### 7. Produce the report

Follow [references/report-template.md](references/report-template.md). Write in the user's language. Lead with the verdict, strengths, and highest-leverage changes. Be direct but respectful. Do not rewrite the entire design or prescribe a new style unless requested.

## Comparison and follow-up

When reviewing variants, score them under the same design contract and explain which better serves the stated objective. Do not choose solely by total score when variants pursue different goals.

Anchor every variant to its exact label/filename and unmistakable visible traits before comparison. Before publishing a recommendation, verify that the written rationale describes the recommended file rather than another variant. Follow [references/multi-artifact.md](references/multi-artifact.md).

When the user supplies a revision, compare only against previously established issues where possible:

- Resolved
- Improved but remaining
- Unchanged
- Newly introduced

Keep the original context and scoring weights stable unless the brief changes.
