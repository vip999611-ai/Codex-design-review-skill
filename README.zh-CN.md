# Codex 设计评审 Skill

[English](README.md)

`design-review` 是一个只读、分级证据驱动的 Codex 视觉设计评审 skill。它可以评审截图、导出设计稿、幻灯片、PDF、Figma 链接及多套设计方案，但不会修改用户提交的源文件。

它把视觉批评与专家启发式检查结合起来，明确区分观察事实、专业推断和未知信息；只对证据充分的维度评分，并可生成问题标注图和低保真优化结构示意。

## 核心能力

- 评审海报、活动 Banner、品牌视觉、IP/角色设计、演示文稿、数据可视化以及 App、Web、后台 UI。
- 按 `S0` 阻断问题到 `S3` 润色建议划分优先级。
- 对高严重度问题标明直接观察、证据来源与置信度。
- 只对可见或有来源支持的维度评分；信息不足时标记为暂定评分。
- 保证书面问题编号与视觉标注编号一致。
- 在同一设计契约下比较多个版本，并跟踪修改后的已解决、仍存在、未变化和新增问题。
- 不回写用户提交的文件或 Figma 设计。

## 安装

### 从 GitHub Release 安装

1. 从[最新 Release](https://github.com/vip999611-ai/codex-design-review-skill/releases/latest)下载 `design-review-v1.0.0.zip` 和对应的 `.sha256` 文件。
2. 如果环境支持，先验证 SHA-256 摘要。
3. 把压缩包解压到 Codex skills 目录。最终目录必须是：

   ```text
   <skills 目录>/design-review/SKILL.md
   ```

个人 skills 的标准位置为：设置了 `CODEX_HOME` 时使用 `$CODEX_HOME/skills`，否则使用 `~/.codex/skills`。

PowerShell 示例：

```powershell
$skillsRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex\skills' }
Expand-Archive .\design-review-v1.0.0.zip -DestinationPath $skillsRoot
Test-Path (Join-Path $skillsRoot 'design-review\SKILL.md')
```

macOS/Linux 示例：

```bash
skills_root="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skills_root"
unzip design-review-v1.0.0.zip -d "$skills_root"
test -f "$skills_root/design-review/SKILL.md"
```

安装后重启 Codex 或新建一个任务，使 skill 列表重新加载。

### 从源码安装

克隆本仓库，然后把完整的 [`design-review`](design-review) 目录复制到上述个人 skills 目录。不要只复制 `SKILL.md`，引用资料和脚本也是 skill 的组成部分。

## 使用方法

上传或链接设计稿，然后显式调用：

```text
使用 $design-review 评审这张面向中国城市年轻用户的活动海报。
优先列出最重要的五个问题，并在可行时生成视觉标注。
```

更多示例：

```text
使用 $design-review 在同一个转化目标下比较这三个首页方案。
```

```text
使用 $design-review 审核这份路演 PDF，把它作为渲染稿评审，不要编辑源文件。
```

```text
使用 $design-review 通过只读工具评审这个 Figma Frame。
```

提供设计目标、受众、投放渠道、最终尺寸或观看距离，以及适用的品牌规则，可以显著提高结论置信度。若缺少的信息会实质改变判断，skill 最多询问三个关键问题；也可以在清楚标注假设后直接继续。

## 输出内容

典型报告包含：

1. 一行设计契约与置信度说明。
2. 总体结论、优势和杠杆最高的调整方向。
3. 默认不超过十条的分级问题，重点突出前五项。
4. 在证据充分时提供正式或暂定加权评分。
5. 在工具和输入允许时提供问题标注图与优化结构示意。
6. 明确列出未知项、需要检查源文件的项目及需要用户测试回答的问题。

证据等级：

- `A`：约束性或官方要求，包括用户提供的项目规则和适用标准。
- `B`：成熟机构或专业体系的指南。
- `C`：从业者经验法，仅用于辅助判断，不能单独构成 `S0` 或 `S1` 问题。

数值评分是对有证据支持的设计维度所作的专家评估，不代表可用性测试、转化预测、市场表现、法律批准、印刷打样或无障碍认证。

## 辅助脚本

### 确定性评分校验

[`validate_score.py`](design-review/scripts/validate_score.py) 只使用 Python 标准库。它通过 `--input` 或标准输入读取 JSON，并向标准输出写入经过校验的结果。

```powershell
@'
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
'@ | python .\design-review\scripts\validate_score.py --pretty
```

无法评估的维度用 `null` 表示。当可支持权重不少于 50 时，脚本会对剩余权重重新归一化；非法权重、越界分数或没有原因的人工调整会以退出码 `2` 失败。

在默认文本编码为 GBK 的 Windows 环境中，调用外部 UTF-8 校验工具时应使用 `python -X utf8 ...`，或仅对该命令设置 `PYTHONUTF8=1`。

### 问题标注图

[`annotate_review.ps1`](design-review/scripts/annotate_review.ps1) 只创建派生 PNG，并禁止输出路径与源文件相同。确定性标注实现依赖 Windows PowerShell 5.1 和 `System.Drawing`。

Marker 文件示例：

```json
[
  {
    "id": "P1",
    "severity": "S1",
    "x": 0.55,
    "y": 0.20,
    "w": 0.35,
    "h": 0.55,
    "label": "人物卡片规则不一致"
  }
]
```

坐标使用 `0` 到 `1` 的归一化值。运行方式：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\design-review\scripts\annotate_review.ps1 `
  -Source .\poster.png `
  -Output .\design-review-output\poster\poster-annotated.png `
  -MarkersPath .\markers.json
```

在 macOS 或 Linux 上，文字报告和评分脚本仍可使用。Codex 可以根据可用工具生成其他形式的派生标注；若没有可靠工具，skill 会退化为精确的文字定位，不会伪造图片结果。

## 只读、安全与隐私边界

- 不修改源设计稿；派生文件写入独立输出目录。
- 本 skill 中的 Figma 操作仅限只读。
- 未经用户明确授权，私密设计素材应保持在本地，不发送到外部服务。
- 不会把截图估算值、隐藏状态、响应式表现、印刷属性或源图层细节冒充为已验证事实。
- 本地已有的评审结果和测试素材不会进入公开仓库或 Release 压缩包。

## 开发与验证

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Windows 额外运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tests\smoke_annotator.ps1
```

如需使用 Codex 随附的校验器，请以 UTF-8 模式运行本地 `quick_validate.py` 并把 `design-review` 目录作为参数。校验器的具体位置取决于本机 Codex 安装。

生成 Release 文件：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\package_release.ps1 -Version 1.0.0
```

## 许可证

[MIT](LICENSE) © 2026 vip999611-ai
