# Standard review report

Use this compact structure. Omit empty sections.

## 评审结论

`[评审模式]｜[作品类型]｜[总分]/100｜[等级]｜[正式/暂定]｜置信度：[高/中/低]`

One paragraph: what works, the central limitation, and whether it is ready for its intended use.

State the assumed design contract: goal, audience, channel/size/viewing context, and applicable specification. Mark assumptions. State explicitly that expert review is not user testing when behavior or preference matters.

## 分项评分

Provide a concise table with dimension, weight, score, weighted points, and one-sentence evidence. Sum weighted points and verify the displayed total. Show `N/A` for unsupported dimensions and say if weights were renormalized.

## 做得好的地方

List 2–4 specific strengths worth preserving. Do not use empty praise.

Name this section `值得保留的设计语言` when the artifact is expressive, experimental, brand-led, or character-led.

## 优先修改 Top 5

For each finding use:

`[S0–S3] 问题名 — 位置；现象；影响；建议动作；证据类型：[直接观察/规范支持/专业推断/待验证]；来源等级：[A/B/C/不适用]；置信度`

Make changes executable. Examples of useful action language:

- Align the subtitle and body to the title's left axis; then test optical compensation at thumbnail scale.
- Reduce competing accent roles from three to one; reserve the accent for the CTA and key number.
- Increase separation between group A and B until the inter-group gap is visibly larger than the internal row gap.
- Replace the topic title with the slide's conclusion and move supporting evidence into the chart annotation.

Use approximate values only when they genuinely help and label them as starting points, not universal laws.

## 其他问题

Include up to five S2/S3 findings, grouped by root cause. Omit if none.

## 推荐修改顺序

Give a 3-stage sequence:

1. Fix purpose/content/accessibility blockers
2. Rebuild hierarchy, grouping, and system
3. Polish type, color, imagery, and micro-alignment

Explain dependencies when changing one item affects others.

## 评审标注图与优化示意

When the artifact can be rendered, include links or rendered previews for:

- `评审标注图｜非修改稿`: the unmodified artwork plus numbered issue markers matching the written Top findings.
- `优化结构示意｜非最终稿`: a low-fidelity hierarchy/layout proposal showing the recommended relationships, not a polished redesign.

For each image, name the exact source filename and explain what the viewer should compare. If the visual aid could not be generated, state the specific reason and provide precise text-based locations. For batches, disclose whether the visual aid covers all artifacts, a representative series contact sheet, or only the highest-priority outliers.

## 复检清单

Give 3–6 artifact-specific checks the designer can perform after revision. Prefer observable pass/fail checks.

## 限制与待确认

List anything a screenshot cannot prove: exact values, source layers, final size, print/export settings, interaction states, brand rules, or data provenance.

Separate into:

- `需源文件/规范验证`
- `建议真实用户验证`

For genuine expert disagreement, add `评审争议` with the competing goals and the condition that changes the recommendation.
