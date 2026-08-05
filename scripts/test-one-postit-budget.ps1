$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$fixture=Join-Path $root 'tests/fixtures/one-postit'
$scratch=Join-Path $root 'tmp/one-postit-budget'
if(Test-Path $scratch){Remove-Item -LiteralPath $scratch -Recurse -Force}
New-Item -ItemType Directory -Force "$scratch/com","$scratch/mapping"|Out-Null
Copy-Item "$fixture/com/BUDGET1-functional-front-p01.json" "$scratch/com/"
Copy-Item "$fixture/mapping/BUDGET1-functional-front-traces.json" "$scratch/mapping/"
& "$PSScriptRoot/validate-skills.ps1"
& "$PSScriptRoot/audit-pipeline.ps1" -DeliveryId BUDGET1 -ComDirectory "$scratch/com" -MappingDirectory "$scratch/mapping"
& "$PSScriptRoot/audit-pipeline.ps1" -DeliveryId BUDGET1 -ComDirectory "$scratch/com" -MappingDirectory "$scratch/mapping" -FalsifiabilityCheck $true
Write-Host 'One-post-it budget: PASS; falsifiability rejection: PASS'
