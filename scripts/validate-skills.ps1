$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$skills = @('7cs-canvas-ingest','7cs-business-context','7cs-architectural-context','7cs-system-context','7cs-structural','7cs-functional-A','7cs-functional-B','7cs-deployment','7cs-com-transform','7cs-spec-compose','7cs-spec-audit','7cs-backend-slice')
foreach ($skill in $skills) {
  $path = Join-Path $root ".agents/skills/$skill/SKILL.md"
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing skill: $skill" }
  $text = Get-Content -Raw -LiteralPath $path -Encoding UTF8
  if ($text -notmatch "(?s)^---\r?\nname:\s+$([regex]::Escape($skill))\r?\ndescription:\s+.+?\r?\n---") { throw "Invalid frontmatter: $skill" }
}
Write-Host "Skills valid: $($skills.Count)"
