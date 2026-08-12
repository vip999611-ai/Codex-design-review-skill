# Codex Design Review Skill

[简体中文](README.zh-CN.md)

`design-review` is a read-only Codex skill for evidence-graded expert critique of visual design. It reviews screenshots, exported artwork, slide decks, PDFs, Figma links, and design variants without editing the submitted source.

It combines visual critique with heuristic inspection, separates observations from inferences and unknowns, assigns supported scores, and can produce annotated issue images and low-fidelity optimization diagrams.

## Highlights

- Reviews posters, campaign banners, brand visuals, IP/character art, presentations, data visualizations, and app/web/admin UI.
- Prioritizes findings from `S0` blockers through `S3` polish.
- Grounds high-severity findings in direct observations or graded sources.
- Scores only visible or otherwise supported dimensions and marks uncertain scores as provisional.
- Keeps written findings synchronized with numbered visual annotations.
- Compares variants under one design contract and tracks resolved, remaining, unchanged, and new issues in revisions.
- Never writes back to the submitted file or Figma design.

## Install

### From a GitHub Release

1. Download `design-review-v1.0.0.zip` and its `.sha256` file from the [latest release](https://github.com/vip999611-ai/codex-design-review-skill/releases/latest).
2. Verify the SHA-256 digest if your environment supports it.
3. Extract the archive into your Codex skills directory. The installed path must end with:

   ```text
   <skills-directory>/design-review/SKILL.md
   ```

The standard personal skills directory is `$CODEX_HOME/skills` when `CODEX_HOME` is configured, otherwise `~/.codex/skills`.

PowerShell example:

```powershell
$skillsRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex\skills' }
Expand-Archive .\design-review-v1.0.0.zip -DestinationPath $skillsRoot
Test-Path (Join-Path $skillsRoot 'design-review\SKILL.md')
```

macOS/Linux example:

```bash
skills_root="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skills_root"
unzip design-review-v1.0.0.zip -d "$skills_root"
test -f "$skills_root/design-review/SKILL.md"
```

Restart Codex or start a new task after installing so the skill catalog refreshes.

### From source

Clone this repository, then copy the complete [`design-review`](design-review) directory into the same personal skills directory. Do not copy only `SKILL.md`; the references and scripts are part of the skill.

## Use

Attach or link the artifact and invoke the skill explicitly:

```text
Use $design-review to review this campaign poster for an urban Chinese audience.
Prioritize the five most important issues and generate visual annotations when possible.
```

Other example requests:

```text
Use $design-review to compare these three homepage variants under the same conversion goal.
```

```text
Use $design-review to audit this pitch deck. Treat the PDF as a rendered artifact and do not edit it.
```

```text
Use $design-review to review this Figma frame through read-only tools only.
```

Providing the goal, audience, channel, final dimensions/viewing distance, and applicable brand rules improves confidence. When these inputs are missing, the skill either asks up to three material questions or proceeds with labeled assumptions.

## What it returns

A typical review includes:

1. A one-line design contract and confidence statement.
2. A verdict, strengths, and the highest-leverage changes.
3. Up to ten prioritized findings, emphasizing the top five.
4. A supported or provisional weighted score when enough evidence exists.
5. An annotated issue image and an optimization diagram when accurate rendering tools are available.
6. Explicit unknowns and items that require source inspection or user testing.

Evidence levels are:

- `A`: governing or official requirements, including supplied project rules and applicable standards.
- `B`: institutional or established professional guidance.
- `C`: practitioner heuristics, used as supporting guidance rather than the sole basis for `S0` or `S1` findings.

The numeric score is an expert assessment of supported design dimensions. It is not a usability-test result, conversion prediction, market-performance score, legal approval, print proof, or accessibility certification.

## Helper scripts

### Deterministic score validation

[`validate_score.py`](design-review/scripts/validate_score.py) uses only the Python standard library. It reads JSON from `--input` or standard input and writes validated JSON to standard output.

```bash
python design-review/scripts/validate_score.py --pretty <<'JSON'
{
  "route": "poster",
  "confidence": "high",
  "dimensions": [
    {"name": "goal", "weight": 25, "score": 8},
    {"name": "hierarchy", "weight": 25, "score": 7},
    {"name": "craft", "weight": 25, "score": 8},
    {"name": "delivery", "weight": 25, "score": 7}
  ]
}
JSON
```

Use `null` for an unsupported dimension. The script renormalizes supported weights only when they total at least 50. Invalid weights, scores, or unexplained manual adjustments fail with exit code `2`.

On Windows systems whose default Python text encoding is GBK, invoke external UTF-8 validation tools with `python -X utf8 ...` or set `PYTHONUTF8=1` for that command.

### Annotated issue images

[`annotate_review.ps1`](design-review/scripts/annotate_review.ps1) creates a derived PNG and never permits the output path to equal the source path. Its deterministic implementation requires Windows PowerShell 5.1 and `System.Drawing`.

Marker file:

```json
[
  {
    "id": "P1",
    "severity": "S1",
    "x": 0.55,
    "y": 0.20,
    "w": 0.35,
    "h": 0.55,
    "label": "Inconsistent card treatment"
  }
]
```

Coordinates are normalized from `0` to `1`. Run it with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\design-review\scripts\annotate_review.ps1 `
  -Source .\poster.png `
  -Output .\design-review-output\poster\poster-annotated.png `
  -MarkersPath .\markers.json
```

On macOS or Linux, the written review and score validation remain available. Codex may use another available image tool for derived annotations; otherwise the skill falls back to precise text-only locations instead of fabricating a visual.

## Safety and privacy

- Source artifacts remain unchanged. Derived files go to a separate output directory.
- Figma access is read-only under this skill.
- Private artwork should remain local unless the user explicitly authorizes an external service.
- Screenshot-derived measurements, contrast estimates, hidden states, responsive behavior, print properties, and source-layer details are never presented as verified facts.
- Existing local review outputs and test artifacts are intentionally excluded from this public repository and from release archives.

## Development and validation

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

On Windows, also run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tests\smoke_annotator.ps1
```

To validate the skill with Codex's bundled validator, run `quick_validate.py` in UTF-8 mode against the `design-review` directory. The exact validator path depends on the local Codex installation.

Create release assets with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\package_release.ps1 -Version 1.0.0
```

## License

[MIT](LICENSE) © 2026 vip999611-ai
