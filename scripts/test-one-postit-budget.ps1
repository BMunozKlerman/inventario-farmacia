$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$fixture=Join-Path $root 'tests/fixtures/one-postit'
$scratch=Join-Path $root 'tmp/one-postit-budget'
if(Test-Path $scratch){Remove-Item -LiteralPath $scratch -Recurse -Force}
New-Item -ItemType Directory -Force "$scratch/com","$scratch/mapping","$scratch/clarifications"|Out-Null
Copy-Item "$fixture/com/BUDGET1-functional-front-p01.json" "$scratch/com/"
Copy-Item "$fixture/mapping/BUDGET1-functional-front-traces.json" "$scratch/mapping/"
& "$PSScriptRoot/validate-skills.ps1"
& "$PSScriptRoot/audit-pipeline.ps1" -DeliveryId BUDGET1 -ComDirectory "$scratch/com" -MappingDirectory "$scratch/mapping"
& "$PSScriptRoot/audit-pipeline.ps1" -DeliveryId BUDGET1 -ComDirectory "$scratch/com" -MappingDirectory "$scratch/mapping" -FalsifiabilityCheck $true
$closed=@{delivery_id='BUDGET1';questions=@()}|ConvertTo-Json
$closed|Set-Content "$scratch/clarifications/BUDGET1-reading.json" -Encoding utf8
$closed|Set-Content "$scratch/clarifications/BUDGET1-transformation.json" -Encoding utf8
& "$PSScriptRoot/audit-pipeline.ps1" -DeliveryId BUDGET1 -ComDirectory "$scratch/com" -MappingDirectory "$scratch/mapping" -ClarificationDirectory "$scratch/clarifications" -RequireClarificationGate $true
$expectedQuestion='¿Qué simbologías de código de barras se aceptarán?'
$open=@{delivery_id='BUDGET1';questions=@(@{id='Q-TEST-001';question=$expectedQuestion;status='open'})}|ConvertTo-Json -Depth 5
$open|Set-Content "$scratch/clarifications/BUDGET1-transformation.json" -Encoding utf8
$decodedQuestion=((Get-Content -LiteralPath "$scratch/clarifications/BUDGET1-transformation.json" -Raw -Encoding UTF8|ConvertFrom-Json).questions)[0].question
if($decodedQuestion -ne $expectedQuestion){throw 'UTF-8 clarification round-trip failed'}
$gateRejected=$false
try { & "$PSScriptRoot/audit-pipeline.ps1" -DeliveryId BUDGET1 -ComDirectory "$scratch/com" -MappingDirectory "$scratch/mapping" -ClarificationDirectory "$scratch/clarifications" -RequireClarificationGate $true }
catch { $gateRejected=$true }
if(-not $gateRejected){throw 'Clarification gate did not reject an open question'}
Write-Host 'One-post-it budget: PASS; falsifiability rejection: PASS; clarification gate: PASS'
