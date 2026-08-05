param([Parameter(Mandatory)][string]$DeliveryId,[string]$ComDirectory='com',[string]$MappingDirectory='mapping',[string]$ClarificationDirectory='clarifications',[bool]$RequireClarificationGate=$false,[bool]$FalsifiabilityCheck=$false)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
function RepoPath($p) { if ([IO.Path]::IsPathRooted($p)) { $p } else { Join-Path $root $p } }
if($RequireClarificationGate){
  $clarificationFiles=@(Get-ChildItem -LiteralPath (RepoPath $ClarificationDirectory) -Filter "$DeliveryId-*.json" -File -ErrorAction SilentlyContinue|Where-Object {$_.Name -match '-(reading|transformation)\.json$'})
  if($clarificationFiles.Count -lt 2){throw "Missing clarification gate files for $DeliveryId"}
  $openQuestions=@($clarificationFiles|ForEach-Object {(Get-Content -LiteralPath $_.FullName -Raw|ConvertFrom-Json).questions}|Where-Object {$_.status -eq 'open'})
  if($openQuestions.Count){throw "Open clarifications for ${DeliveryId}: $($openQuestions.Count)"}
}
$comFiles = @(Get-ChildItem -LiteralPath (RepoPath $ComDirectory) -Filter "$DeliveryId-*.json" -File -ErrorAction SilentlyContinue)
if (-not $comFiles) { throw "No COM files for $DeliveryId" }
$stickies = @($comFiles | ForEach-Object { $c=Get-Content -Raw $_.FullName|ConvertFrom-Json; @($c.sections)|ForEach-Object{@($_.stickies)|ForEach-Object{$_.id}} } | Sort-Object -Unique)
$traceFiles = @(Get-ChildItem -LiteralPath (RepoPath $MappingDirectory) -Filter "$DeliveryId-*-traces.json" -File -ErrorAction SilentlyContinue)
$traces = @($traceFiles | ForEach-Object { $t=Get-Content -Raw $_.FullName|ConvertFrom-Json; if($t.traces){@($t.traces)}else{@($t)} } | ForEach-Object {$_.sticky_id} | Where-Object {$_ -in $stickies} | Sort-Object -Unique)
$covered = if($FalsifiabilityCheck){[Math]::Max(0, $stickies.Count-1)}else{$traces.Count}
$coverage = if($stickies.Count){$covered/$stickies.Count}else{1}
$passed = $coverage -eq 1
Write-Host "Audit ${DeliveryId}: $(if($passed){'PASS'}else{'FAIL'}) C=$coverage"
if(-not $passed -and -not $FalsifiabilityCheck){exit 1}
if($FalsifiabilityCheck -and $passed){throw 'Falsifiability check did not reject missing trace'}
