# Visual annotation and optimization diagrams

Use this module whenever the review output includes visual aids. The goal is to make findings faster to understand without altering the submitted design or pretending that a diagram is a finished redesign.

## Required outputs

### 1. Annotated issue image

Use the submitted artwork as an unchanged base layer. Add only review overlays:

- Number the prioritized findings `P1` to `P5` and use the same identifiers in the written report.
- Prefer short labels of 2–10 words; put full reasoning in the report.
- Use boxes for regions, arrows for movement or alignment, lines for axes, and translucent areas for density, safe-area, or contrast-risk zones.
- Use severity colors consistently: S0 red, S1 orange, S2 yellow, S3 blue. Do not rely on color alone; always include the severity and marker number in text.
- Keep the artwork readable. Move long labels into a side legend instead of covering essential content.
- Preserve the source aspect ratio. Include the exact filename and the label `评审标注图｜非修改稿`.

The annotation image is evidence mapping, not decoration. Do not add findings that are absent from the report, and do not use a marker to imply an exact measurement that was not verified.

### 2. Optimization diagram

Show the proposed relationships rather than simulating a production-ready redesign:

- Preserve the design contract and intentional visual language identified in the review.
- Demonstrate hierarchy, grouping, alignment, reading path, relative scale, crop, whitespace, or safe-area changes with simplified blocks, guides, or a transparent overlay.
- Reuse real copy only when it can be reproduced accurately. Otherwise use labeled placeholders such as `主标题`, `人物信息`, or `CTA`; never invent campaign claims, legal copy, brand assets, data, or product information.
- Do not redraw logos, faces, characters, charts, or copyrighted artwork as if they were approved final assets.
- If generative image tools are used, restrict them to clearly labeled conceptual mood/layout exploration. Do not present generated text, logos, data, or character details as faithful corrections.
- Include before/after reading-path arrows or a compact legend when the change is not self-evident.
- Label the image `优化结构示意｜非最终稿` and name the source filename.

When only a micro-level or source-only change is needed, such as alternative text, font licensing, exact contrast, export settings, or object reading order, mark it `无法在截图示意中验证` instead of inventing a visible correction.

## Output safety

- Never overwrite the submitted file. Write derived files to a separate workspace folder such as `design-review-output/<source-stem>/`.
- For Figma, presentation, PDF, or document sources, annotate an exported screenshot or rendered page only. Never write the annotation into the source file under this skill.
- Keep private or sensitive artwork local unless the user authorizes an external service. Prefer deterministic local overlays for annotations.
- Inspect the generated images before delivery. Verify marker-to-finding mapping, filename, orientation, crop, text accuracy, and legibility.

For deterministic raster overlays, prefer `scripts/annotate_review.ps1`. On systems that restrict PowerShell scripts, invoke it through `powershell -NoProfile -ExecutionPolicy Bypass -File ...`. Pass a UTF-8 marker file with `-MarkersPath`; normalized `x`, `y`, `w`, and `h` values from 0 to 1 keep annotations resolution-independent. Example marker input:

```json
[
  {"id":"P1","severity":"S1","x":0.55,"y":0.2,"w":0.35,"h":0.55,"label":"人物卡片规则不一致"}
]
```

Always inspect the PNG produced by the script. Use a separate output path and never pass the source path as output.

## Batch behavior

For more than five artifacts, avoid producing two images per artifact unless requested. Default to:

1. A contact sheet that marks series-wide invariant drift and identifies exact filenames.
2. Individual annotation and optimization images for up to three highest-severity or most representative artifacts.
3. A statement listing which artifacts were not individually visualized.

Do not average away an outlier. If one design has an S0/S1 issue, give it an individual annotation even when the rest of the series uses a contact sheet.

## Fallback

If the artifact cannot be rendered, the resolution is insufficient, required tools are unavailable, or a generated diagram would be misleading:

- Complete the written review.
- State why the image was not generated.
- Give precise locations using visible anchors, approximate regions, or page/frame names.
- Offer to generate the visual aids when a clearer export or source-safe screenshot is supplied.
