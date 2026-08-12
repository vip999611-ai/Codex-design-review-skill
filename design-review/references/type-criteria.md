# Type-specific review criteria

Read only the matching section after the universal criteria.

## Poster and campaign/banner

Prioritize stopping power, immediate message, brand/product recognition, emotional tone, CTA/event facts, and channel crop behavior.

Check:

- One dominant hook survives thumbnail/feed or viewing-distance conditions.
- Headline, subject, supporting proof, CTA, date/location/legal copy form a deliberate reading sequence.
- Type and image interact rather than merely occupy separate halves.
- Decorative density reinforces the concept without masking essentials.
- The crop remains viable across required placements; logos and essential copy stay out of unsafe zones.
- Series assets share recognizable invariants.
- Verify copy hierarchy against the campaign job: awareness, information, attendance, acquisition, sale, or retention. Do not judge a brand-awareness key visual like a dense product menu.
- Treat feed thumbnail, outdoor distance, physical print, and in-store close reading as different contracts; recommend the channel-specific test.

Allow experimental typography, asymmetry, overlaps, texture, and saturated palettes when message and deliberate system remain clear.

## Brand visual system

Prioritize recognizability, distinctiveness, coherence, flexibility, and governance.

Check:

- Brand strategy and personality are visible through a repeatable visual grammar.
- Logo approved variants, clear space, minimum size, proportion, color use, background suitability, and misuse constraints are respected when guidelines exist.
- Color, typography, imagery, illustration, icon, shape, layout, and motion cues feel related.
- Voice, terminology, and message tone remain consistent with the visual identity when copy is present.
- The system can stretch from quiet to expressive applications without losing identity.
- It is distinguishable from category clichés and does not depend on a single decorative trick.
- Across media, distinguish required invariants from intentionally flexible expressions; consistency does not mean identical layouts.

Do not penalize deviation from generic conventions when it is defined by the brand system.
Treat brand compliance as **needs verification** unless the approved guide and asset package are supplied. Without them, assess coherence and likely fit, not compliance.

## IP and character visual

Prioritize silhouette recognition, character identity, emotional expression, construction consistency, and cross-medium adaptability.

Check:

- Compare silhouette, key proportions, face/feature placement, signature colors, props, motifs, and personality traits with the supplied model sheet/character bible when available.
- Front/side/three-quarter views, poses, and expressions preserve construction logic.
- Line weight, shape language, material, lighting, rendering detail, and texture are coherent.
- Accessories and background support rather than obscure the character.
- Small-size, monochrome, merchandise, animation, and 3D translation risks are considered when relevant.
- Flag unauthorized model-shape changes only when a source character bible or reference exists.

Treat silhouette clarity, shape language, appeal, and pose readability as C-level heuristics unless the project specification makes them requirements. Without a model sheet, never claim that the character is "off-model", "drawn wrong", or has unauthorized proportion changes. Instead assess internal coherence and request canonical views. Allow expressive deformation when it is consistent with the character's motion/style contract.

## Presentation/PPT

Prioritize narrative, one-slide purpose, projection legibility, scanability, and deck-wide consistency.

Check:

- Each slide has one clear takeaway expressible as a sentence.
- Titles communicate conclusions when the presentation is analytical, not merely topics.
- Content density suits live speaking versus self-reading use.
- Type can be read at expected room/device distance; body copy is not treated like a document page.
- Images, charts, and diagrams carry meaning; decoration does not consume attention.
- Layout, master elements, page numbers, source notes, chart styles, and transitions are consistent.
- Across slides, pacing alternates appropriately among setup, evidence, emphasis, and conclusion.
- Every meaningful slide has a unique, informative title in the source deck; analytical slides should prefer conclusion-led titles when appropriate.
- Source-deck object reading order follows the intended meaning, complex diagrams are grouped logically, informative visuals have useful alternative text, and decorative objects are marked decorative.
- Run PowerPoint's Accessibility Checker on the source deck; visual inspection alone cannot certify reading order, alternative text, theme semantics, or screen-reader output.

Review a single slide provisionally; do not score deck narrative or consistency without multiple slides.
From a screenshot, assess only visual reading order. Mark source reading order, alternative text, slide-title metadata, animation, and Accessibility Checker results as **needs verification** and N/A for scoring unless inspected.

## Data visualization and dashboard

Prioritize truthfulness, clarity, correct encoding, meaningful comparison, annotation, accessibility, and decision support.

Check:

- The chart type matches the question: trend, comparison, distribution, relationship, composition, geography, or flow.
- Scale, baseline, intervals, axes, units, denominators, sample size, time range, and uncertainty are truthful and visible where necessary.
- Area/volume/3D effects do not exaggerate magnitude; dual axes and truncated axes have strong justification.
- Sorting, grouping, aggregation, and color categories support the intended comparison.
- Labels and direct annotations reduce legend lookup; highlight only the insight that matters.
- Titles should communicate the main insight or question; labels and legends should explain mappings of color, shape, size, and line style concisely. Prefer direct labels when they reduce lookup without clutter.
- Axes, ticks, gridlines, and units should clarify proportion and scale without overwhelming the data.
- Color is not the only discriminator; use labels, shapes, patterns, or line styles.
- Source, date, definitions, filters, and freshness are present where decision-making depends on them.
- Dashboard hierarchy separates headline indicators, context, diagnostics, filters, and detail; it supports a defined user task rather than displaying every metric.
- For interactive visualizations, support overview first, filtering/zoom where useful, and details on demand. Do not hide essential interpretation behind hover or interaction alone.
- Use categorical palettes for unrelated groups and sequential/diverging palettes for ordered quantities or deviations when appropriate; verify cultural and semantic implications.
- Provide underlying data or a text/table alternative for accessibility when published digitally.

Treat misleading data representation as S0 even if visually polished.
Before assigning S0, distinguish a demonstrably misleading encoding from a merely suboptimal chart choice. Verify source data and transformation when the visible chart alone cannot prove the discrepancy.

## UI: app, web, or admin

This is a secondary route. Prioritize task completion, states, interaction clarity, design-system consistency, responsive behavior, and accessibility.

Check:

- Page purpose, primary action, navigation, labels, status, feedback, errors, empty/loading states, and destructive actions.
- Component variants, tokens, spacing, type, icons, radius, elevation, and semantic color are consistent.
- Touch/pointer targets and spacing are usable. WCAG 2.2 AA defines a 24×24 CSS-pixel minimum target or sufficient spacing, with exceptions; platform guidance may recommend larger.
- Keyboard/focus/order, zoom/reflow, localization, dynamic type, and responsive behavior require source/prototype evidence; do not infer from one static screen.
- Admin tables optimize scanning, comparison, alignment of numbers, column priority, filters, bulk actions, and density without sacrificing legibility.
