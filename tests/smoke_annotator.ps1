$ErrorActionPreference = 'Stop'

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$annotator = Join-Path $repositoryRoot 'design-review\scripts\annotate_review.ps1'
$workingDirectory = Join-Path ([System.IO.Path]::GetTempPath()) ("design-review-smoke-" + [guid]::NewGuid().ToString('N'))

New-Item -ItemType Directory -Path $workingDirectory | Out-Null
try {
    Add-Type -AssemblyName System.Drawing

    $source = Join-Path $workingDirectory 'source.png'
    $output = Join-Path $workingDirectory 'annotated.png'
    $markers = Join-Path $workingDirectory 'markers.json'

    $bitmap = New-Object System.Drawing.Bitmap(640, 360)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    try {
        $graphics.Clear([System.Drawing.Color]::FromArgb(255, 245, 247, 250))
        $brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 37, 99, 235))
        try {
            $graphics.FillRectangle($brush, 120, 100, 400, 160)
        } finally {
            $brush.Dispose()
        }
        $bitmap.Save($source, [System.Drawing.Imaging.ImageFormat]::Png)
    } finally {
        $graphics.Dispose()
        $bitmap.Dispose()
    }

    '[{"id":"P1","severity":"S1","x":0.18,"y":0.25,"w":0.64,"h":0.50,"label":"Smoke test marker"}]' |
        Set-Content -LiteralPath $markers -Encoding UTF8

    $sourceHashBefore = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash
    & $annotator -Source $source -Output $output -MarkersPath $markers
    $sourceHashAfter = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash

    if ($sourceHashBefore -ne $sourceHashAfter) {
        throw 'The annotator modified the source image.'
    }
    if (-not (Test-Path -LiteralPath $output)) {
        throw 'The annotator did not create an output PNG.'
    }
    if ((Get-Item -LiteralPath $output).Length -le 0) {
        throw 'The annotator created an empty output file.'
    }

    Write-Host 'Annotator smoke test passed.'
} finally {
    if (Test-Path -LiteralPath $workingDirectory) {
        Remove-Item -LiteralPath $workingDirectory -Recurse -Force
    }
}
