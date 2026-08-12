param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^\d+\.\d+\.\d+$')]
    [string]$Version
)

$ErrorActionPreference = 'Stop'

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$skillSource = Join-Path $repositoryRoot 'design-review'
$licenseSource = Join-Path $repositoryRoot 'LICENSE'
$dist = Join-Path $repositoryRoot 'dist'
$stageRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("design-review-package-" + [guid]::NewGuid().ToString('N'))
$stageSkill = Join-Path $stageRoot 'design-review'
$archive = Join-Path $dist ("design-review-v$Version.zip")
$checksum = "$archive.sha256"

if (-not (Test-Path -LiteralPath (Join-Path $skillSource 'SKILL.md'))) {
    throw "Skill source is incomplete: $skillSource"
}

New-Item -ItemType Directory -Path $dist -Force | Out-Null
if (Test-Path -LiteralPath $archive) {
    Remove-Item -LiteralPath $archive -Force
}
if (Test-Path -LiteralPath $checksum) {
    Remove-Item -LiteralPath $checksum -Force
}

New-Item -ItemType Directory -Path $stageRoot | Out-Null
try {
    Copy-Item -LiteralPath $skillSource -Destination $stageSkill -Recurse
    Copy-Item -LiteralPath $licenseSource -Destination (Join-Path $stageSkill 'LICENSE')

    Get-ChildItem -LiteralPath $stageSkill -Recurse -Directory -Force |
        Where-Object { $_.Name -in @('__pycache__', '.pytest_cache') } |
        Sort-Object FullName -Descending |
        Remove-Item -Recurse -Force
    Get-ChildItem -LiteralPath $stageSkill -Recurse -File -Force |
        Where-Object { $_.Extension -in @('.pyc', '.pyo') } |
        Remove-Item -Force

    Compress-Archive -LiteralPath $stageSkill -DestinationPath $archive -CompressionLevel Optimal
    $hash = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant()
    "$hash  $([System.IO.Path]::GetFileName($archive))" |
        Set-Content -LiteralPath $checksum -Encoding ASCII -NoNewline
} finally {
    if (Test-Path -LiteralPath $stageRoot) {
        Remove-Item -LiteralPath $stageRoot -Recurse -Force
    }
}

Write-Host "Created $archive"
Write-Host "Created $checksum"
