param(
    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Output,

    [string]$MarkersJson,

    [string]$MarkersPath,

    [switch]$Force
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$sourcePath = [System.IO.Path]::GetFullPath($Source)
$outputPath = [System.IO.Path]::GetFullPath($Output)

if (-not [System.IO.File]::Exists($sourcePath)) {
    throw "Source image not found: $sourcePath"
}
if ($sourcePath -eq $outputPath) {
    throw 'Output must be a derived copy, not the source image.'
}
if ([System.IO.Path]::GetExtension($outputPath).ToLowerInvariant() -ne '.png') {
    throw 'Output must use the .png extension.'
}
if ([System.IO.File]::Exists($outputPath) -and -not $Force) {
    throw "Output already exists. Pass -Force only when replacing a derived review image: $outputPath"
}

if (-not [string]::IsNullOrWhiteSpace($MarkersPath)) {
    $resolvedMarkersPath = [System.IO.Path]::GetFullPath($MarkersPath)
    if (-not [System.IO.File]::Exists($resolvedMarkersPath)) {
        throw "Markers file not found: $resolvedMarkersPath"
    }
    $markerText = [System.IO.File]::ReadAllText($resolvedMarkersPath, [System.Text.Encoding]::UTF8)
} elseif (-not [string]::IsNullOrWhiteSpace($MarkersJson)) {
    $markerText = $MarkersJson
} else {
    throw 'Pass either -MarkersPath or -MarkersJson.'
}
$parsedMarkers = ConvertFrom-Json -InputObject $markerText
$markers = @()
foreach ($item in $parsedMarkers) {
    $markers += $item
}
if ($markers.Count -eq 0) {
    throw 'At least one marker is required.'
}

$severityColors = @{
    S0 = [System.Drawing.Color]::FromArgb(255, 220, 38, 38)
    S1 = [System.Drawing.Color]::FromArgb(255, 249, 115, 22)
    S2 = [System.Drawing.Color]::FromArgb(255, 234, 179, 8)
    S3 = [System.Drawing.Color]::FromArgb(255, 37, 99, 235)
}

$sourceImage = [System.Drawing.Image]::FromFile($sourcePath)
$bitmap = New-Object System.Drawing.Bitmap($sourceImage.Width, $sourceImage.Height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.DrawImage($sourceImage, 0, 0, $sourceImage.Width, $sourceImage.Height)

$scale = [Math]::Max(1.0, [Math]::Min($sourceImage.Width, $sourceImage.Height) / 900.0)
$lineWidth = [Math]::Max(3.0, 4.0 * $scale)
$fontSize = [Math]::Max(13.0, 18.0 * $scale)
$smallFontSize = [Math]::Max(11.0, 14.0 * $scale)
$font = New-Object System.Drawing.Font('Microsoft YaHei UI', $fontSize, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
$smallFont = New-Object System.Drawing.Font('Microsoft YaHei UI', $smallFontSize, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)

$reviewLabel = -join @(
    [char]0x8BC4, [char]0x5BA1, [char]0x6807, [char]0x6CE8, [char]0x56FE,
    [char]0xFF5C,
    [char]0x975E, [char]0x4FEE, [char]0x6539, [char]0x7A3F
)
$fileName = [System.IO.Path]::GetFileName($sourcePath)
$title = "$reviewLabel | $fileName"
$titleSize = $graphics.MeasureString($title, $smallFont)
$titlePad = [Math]::Max(8.0, 10.0 * $scale)
$titleBox = New-Object System.Drawing.RectangleF(0, 0, ($titleSize.Width + 2 * $titlePad), ($titleSize.Height + 2 * $titlePad))
$titleBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(200, 17, 24, 39))
$whiteBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$graphics.FillRectangle($titleBrush, $titleBox)
$graphics.DrawString($title, $smallFont, $whiteBrush, $titlePad, $titlePad)

foreach ($marker in $markers) {
    $id = [string]$marker.id
    $severity = ([string]$marker.severity).ToUpperInvariant()
    $label = [string]$marker.label
    if ([string]::IsNullOrWhiteSpace($id) -or [string]::IsNullOrWhiteSpace($label)) {
        throw 'Every marker requires id and label.'
    }
    if (-not $severityColors.ContainsKey($severity)) {
        throw "Unsupported severity '$severity'. Use S0, S1, S2, or S3."
    }

    $values = @([double]$marker.x, [double]$marker.y, [double]$marker.w, [double]$marker.h)
    foreach ($value in $values) {
        if ($value -lt 0 -or $value -gt 1) {
            throw 'Marker x, y, w, and h must use normalized values from 0 to 1.'
        }
    }
    if (($values[0] + $values[2]) -gt 1.0001 -or ($values[1] + $values[3]) -gt 1.0001) {
        throw 'Marker rectangle extends outside the image.'
    }

    $color = $severityColors[$severity]
    $x = $values[0] * $sourceImage.Width
    $y = $values[1] * $sourceImage.Height
    $w = [Math]::Max(1, $values[2] * $sourceImage.Width)
    $h = [Math]::Max(1, $values[3] * $sourceImage.Height)

    $pen = New-Object System.Drawing.Pen($color, $lineWidth)
    $fill = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(35, $color.R, $color.G, $color.B))
    $graphics.FillRectangle($fill, $x, $y, $w, $h)
    $graphics.DrawRectangle($pen, $x, $y, $w, $h)

    $markerText = "$id $severity"
    $markerSize = $graphics.MeasureString($markerText, $font)
    $bubbleSize = [Math]::Max($markerSize.Width, $markerSize.Height) + 14 * $scale
    $bubbleX = [Math]::Max(0, [Math]::Min($sourceImage.Width - $bubbleSize, $x - $bubbleSize / 2))
    $bubbleY = [Math]::Max($titleBox.Height, [Math]::Min($sourceImage.Height - $bubbleSize, $y - $bubbleSize / 2))
    $bubbleRect = New-Object System.Drawing.RectangleF($bubbleX, $bubbleY, $bubbleSize, $bubbleSize)
    $bubbleBrush = New-Object System.Drawing.SolidBrush($color)
    $graphics.FillEllipse($bubbleBrush, $bubbleRect)
    $graphics.DrawString($markerText, $font, $whiteBrush, ($bubbleX + 7 * $scale), ($bubbleY + 6 * $scale))

    $labelText = "$id $label"
    $labelSize = $graphics.MeasureString($labelText, $smallFont)
    $labelWidth = [Math]::Min($sourceImage.Width * 0.45, $labelSize.Width + 2 * $titlePad)
    $labelHeight = $labelSize.Height + 2 * $titlePad
    $labelX = [Math]::Max(0, [Math]::Min($sourceImage.Width - $labelWidth, $x))
    $labelY = [Math]::Max($titleBox.Height, [Math]::Min($sourceImage.Height - $labelHeight, $y + $h + 4 * $scale))
    $labelRect = New-Object System.Drawing.RectangleF($labelX, $labelY, $labelWidth, $labelHeight)
    $labelBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(220, 17, 24, 39))
    $graphics.FillRectangle($labelBrush, $labelRect)
    $graphics.DrawString($labelText, $smallFont, $whiteBrush, ($labelX + $titlePad), ($labelY + $titlePad))

    $pen.Dispose()
    $fill.Dispose()
    $bubbleBrush.Dispose()
    $labelBrush.Dispose()
}

$outputDirectory = [System.IO.Path]::GetDirectoryName($outputPath)
if (-not [System.IO.Directory]::Exists($outputDirectory)) {
    [System.IO.Directory]::CreateDirectory($outputDirectory) | Out-Null
}
$bitmap.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)

$font.Dispose()
$smallFont.Dispose()
$titleBrush.Dispose()
$whiteBrush.Dispose()
$graphics.Dispose()
$bitmap.Dispose()
$sourceImage.Dispose()

Write-Output $outputPath
