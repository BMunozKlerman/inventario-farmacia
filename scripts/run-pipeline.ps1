[CmdletBinding()]
param(
  [Parameter(Mandatory)][string]$PdfPath,
  [Parameter(Mandatory)][ValidatePattern('^[A-Za-z0-9_-]+$')][string]$DeliveryId,
  [string]$BudgetPath = 'config/com-budget.json',
  [switch]$KeepExisting,
  [switch]$ComOnly
)

$ErrorActionPreference='Stop'
$root=[IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
function RepoPath($p){if([IO.Path]::IsPathRooted($p)){[IO.Path]::GetFullPath($p)}else{[IO.Path]::GetFullPath((Join-Path $root $p))}}

$pdf=RepoPath $PdfPath
$resources=(RepoPath 'resources').TrimEnd('\')+'\'
if(-not $pdf.StartsWith($resources,[StringComparison]::OrdinalIgnoreCase)){throw 'El PDF debe estar dentro de resources/'}
if(-not(Test-Path -LiteralPath $pdf -PathType Leaf)){throw "PDF no encontrado: $pdf"}

$codex=Get-Command codex -ErrorAction SilentlyContinue
$codexExe=if($codex){$codex.Source}else{
  Get-ChildItem (Join-Path $env:USERPROFILE '.vscode/extensions') -Directory -Filter 'openai.chatgpt-*-win32-x64' -ErrorAction SilentlyContinue |
    Sort-Object Name -Descending |
    ForEach-Object {Join-Path $_.FullName 'bin/windows-x86_64/codex.exe'} |
    Where-Object {Test-Path -LiteralPath $_ -PathType Leaf} |
    Select-Object -First 1
}
if(-not $codexExe){throw 'Codex CLI no está disponible. Instala la extensión oficial de OpenAI para VS Code o agrega codex.exe al PATH.'}

$previousErrorAction=$ErrorActionPreference
try{$ErrorActionPreference='Continue'; & $codexExe login status 2>&1|Out-Null; $loginExitCode=$LASTEXITCODE}
finally{$ErrorActionPreference=$previousErrorAction}
if($loginExitCode -ne 0){throw 'Codex CLI no tiene una sesión activa. Ejecuta codex login.'}

$renderer=Get-ChildItem (RepoPath 'tools/poppler') -Recurse -Filter pdftoppm.exe -File -ErrorAction SilentlyContinue|Select-Object -First 1
if(-not $renderer){$renderer=Get-Command pdftoppm -ErrorAction SilentlyContinue}
if(-not $renderer){throw 'Poppler no está disponible: falta pdftoppm.exe'}
$rendererExe=if($renderer.Source){$renderer.Source}else{$renderer.FullName}

function Invoke-CodexPrompt([string]$Prompt,[array]$ImagePaths=@()){
  $codexArgs=@('exec','--ephemeral','--color','never','-s','workspace-write','-C',$root)
  foreach($image in $ImagePaths){$codexArgs+=@('-i',$image)}
  $oldAction=$ErrorActionPreference
  try{$ErrorActionPreference='Continue'; $Prompt|& $codexExe @codexArgs '-'; $exitCode=$LASTEXITCODE}
  finally{$ErrorActionPreference=$oldAction}
  if($exitCode -ne 0){throw "codex exec falló: $exitCode"}
}

function Get-OpenQuestions([string]$Path){
  if(-not(Test-Path -LiteralPath $Path -PathType Leaf)){throw "Codex no generó el archivo de aclaraciones: $Path"}
  $document=Get-Content -LiteralPath $Path -Raw|ConvertFrom-Json
  @($document.questions|Where-Object {$_.status -eq 'open'})
}

function Request-Answers([string]$Phase,[array]$Questions){
  $answersPath=RepoPath "clarifications/$DeliveryId-answers.json"
  $responses=@()
  if(Test-Path -LiteralPath $answersPath){$responses=@((Get-Content -LiteralPath $answersPath -Raw|ConvertFrom-Json).responses)}
  Write-Host ''
  Write-Host "PIPELINE PAUSADO: se requieren $($Questions.Count) aclaraciones ($Phase)." -ForegroundColor Yellow
  foreach($question in $Questions){
    Write-Host ''
    Write-Host "[$($question.id)] $($question.question)" -ForegroundColor Cyan
    if($question.reason){Write-Host "Motivo: $($question.reason)"}
    do {
      $answer=Read-Host 'Respuesta (o :abort para detener y conservar el estado)'
      if($answer -eq ':abort'){throw 'Ejecución detenida por el usuario durante las aclaraciones.'}
      if([string]::IsNullOrWhiteSpace($answer)){Write-Host 'La respuesta no puede estar vacía.' -ForegroundColor Yellow}
    } while([string]::IsNullOrWhiteSpace($answer))
    $responses+=@{phase=$Phase;question_id=$question.id;question=$question.question;answer=$answer;answered_at=(Get-Date).ToString('o')}
    @{delivery_id=$DeliveryId;responses=$responses}|ConvertTo-Json -Depth 10|Set-Content -LiteralPath $answersPath -Encoding utf8
  }
}

$dirs=@('evidence','com','mapping','composed','audit','clarifications')
foreach($d in $dirs){New-Item -ItemType Directory -Force (RepoPath $d)|Out-Null}
if(-not $KeepExisting){
  foreach($d in $dirs){
    $base=(RepoPath $d).TrimEnd('\')+'\'
    foreach($file in @(Get-ChildItem -LiteralPath $base -Filter "$DeliveryId-*" -File -ErrorAction SilentlyContinue)){
      if(-not $file.FullName.StartsWith($base,[StringComparison]::OrdinalIgnoreCase)){throw 'Ruta de limpieza insegura'}
      Remove-Item -LiteralPath $file.FullName -Force
    }
  }
}

Write-Host '[1/6] Renderizando el PDF localmente'
$prefix=Join-Path (RepoPath 'evidence') "$DeliveryId-page"
& $rendererExe -png -r 180 $pdf $prefix
if($LASTEXITCODE -ne 0){throw "pdftoppm falló: $LASTEXITCODE"}
$rendered=@(Get-ChildItem (RepoPath 'evidence') -Filter "$DeliveryId-page-*.png" -File|Sort-Object Name)
if(-not $rendered){throw 'No se generaron imágenes desde el PDF'}
$pages=@()
for($i=0;$i -lt $rendered.Count;$i++){
  $target=Join-Path (RepoPath 'evidence') ("$DeliveryId-p{0:D2}.png"-f($i+1))
  Move-Item -LiteralPath $rendered[$i].FullName -Destination $target -Force
  $pages+=@{page=$i+1;evidence=(Resolve-Path -Relative $target);status='pending'}
}
$sourceHash=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
@{delivery_id=$DeliveryId;source="resources/$([IO.Path]::GetFileName($pdf))";source_sha256=$sourceHash;pages=$pages}|ConvertTo-Json -Depth 10|Set-Content -LiteralPath (Join-Path (RepoPath 'evidence') "$DeliveryId-page-index.json") -Encoding utf8
$images=@(Get-ChildItem (RepoPath 'evidence') -Filter "$DeliveryId-p*.png" -File|Sort-Object Name|ForEach-Object FullName)

Write-Host '[2/6] Leyendo canvas y generando COM'
$readingQuestions=RepoPath "clarifications/$DeliveryId-reading.json"
$readingPrompt=@"
Procesa el delivery '$DeliveryId' desde las imágenes adjuntas del PDF resources/$([IO.Path]::GetFileName($pdf)). Aplica 7cs-canvas-ingest y entrega cada candidato a los siete lectores locales. Genera exclusivamente COM literales en com/ e informe e índice en evidence/. No transformes, compongas ni audites.

Escribe siempre clarifications/$DeliveryId-reading.json con {"delivery_id":"$DeliveryId","phase":"reading","questions":[]}. Ante texto ilegible, clasificación insegura o datos imprescindibles ambiguos, agrega preguntas concretas con {"id","question","reason","status":"open"}, usa ids estables Q-READ-NNN y no adivines. Si existen respuestas en clarifications/$DeliveryId-answers.json, analízalas junto con la imagen: marca la pregunta resolved sólo si la respuesta permite una transcripción o clasificación inequívoca; de lo contrario mantenla open y reformúlala.

No modifiques resources/, .agents/, scripts/, config/, tests/, tools/, README.md ni AGENTS.md.
"@
Invoke-CodexPrompt $readingPrompt $images
while($true){
  $open=@(Get-OpenQuestions $readingQuestions)
  if($open.Count -eq 0){break}
  Request-Answers 'reading' $open
  Invoke-CodexPrompt $readingPrompt $images
}

Write-Host '[3/6] Validando los COM presupuestados'
$budget=Get-Content -LiteralPath (RepoPath $BudgetPath) -Raw|ConvertFrom-Json
$counts=@{business_context=0;architectural_context=0;system_context=0;structural=0;functional_front=0;functional_back=0;deployment=0}
$ids=@();$comFiles=@(Get-ChildItem (RepoPath 'com') -Filter "$DeliveryId-*.json" -File)
if(-not $comFiles){throw 'Codex no generó COM'}
foreach($file in $comFiles){
  $com=Get-Content -LiteralPath $file.FullName -Raw|ConvertFrom-Json
  $key=if($com.canvas -eq 'functional'){"functional_$($com.variant)"}else{$com.canvas}
  if($counts.ContainsKey($key)){$counts[$key]++}
  foreach($section in @($com.sections)){foreach($sticky in @($section.stickies)){
    if(-not $sticky.id -or -not $sticky.text -or @($sticky.bbox).Count -ne 4){throw "Post-it inválido en $($file.Name)"}
    $ids+=$sticky.id
  }}
}
foreach($entry in $budget.PSObject.Properties){
  Write-Host "  $($entry.Name): $($counts[$entry.Name])/$($entry.Value)"
  if($counts[$entry.Name] -ne [int]$entry.Value){throw "Presupuesto COM incumplido: $($entry.Name)"}
}
if(@($ids|Group-Object|Where-Object Count -gt 1)){throw 'Existen IDs de post-it duplicados'}
Write-Host "  post-its: $($ids.Count)"

if($ComOnly){Write-Host '[4/6] Transformación omitida';Write-Host '[5/6] Composición omitida';Write-Host '[6/6] PDF -> COM: PASS';exit 0}

Write-Host '[4/6] Transformando COM con compuerta de aclaraciones'
$transformationQuestions=RepoPath "clarifications/$DeliveryId-transformation.json"
$transformPrompt=@"
Procesa el delivery '$DeliveryId' usando 7cs-com-transform. Lee únicamente com/$DeliveryId-*.json y, si existe, clarifications/$DeliveryId-answers.json. Genera o reemplaza los artefactos mapping/$DeliveryId-*; no leas el PDF ni evidence/ y no compongas todavía.

Escribe siempre clarifications/$DeliveryId-transformation.json con {"delivery_id":"$DeliveryId","phase":"transformation","questions":[]}. Toda decisión ausente que impida requisitos verificables debe ser una pregunta concreta {"id","question","reason","status":"open"} con id estable Q-TRANS-NNN. Analiza cada respuesta contra los COM: marca resolved sólo si es suficiente; si no, mantén open y reformula la pregunta. No inventes. No continúes a composición.
"@
Invoke-CodexPrompt $transformPrompt
while($true){
  $open=@(Get-OpenQuestions $transformationQuestions)
  if($open.Count -eq 0){break}
  Request-Answers 'transformation' $open
  Invoke-CodexPrompt $transformPrompt
}

Write-Host '[5/6] Componiendo el entregable'
$composePrompt=@"
Compone el delivery '$DeliveryId' mediante 7cs-spec-compose. Lee sólo mapping/$DeliveryId-*, clarifications/$DeliveryId-transformation.json y clarifications/$DeliveryId-answers.json. Verifica que no existan preguntas open; si existe alguna, falla sin escribir composed/. Si la compuerta está cerrada, genera todos los artefactos composed/$DeliveryId-* y déjalos listos para 7cs-spec-audit. No leas el PDF ni evidence/.
"@
Invoke-CodexPrompt $composePrompt

Write-Host '[6/6] Ejecutando auditoría determinista'
& (Join-Path $PSScriptRoot 'audit-pipeline.ps1') -DeliveryId $DeliveryId -RequireClarificationGate $true
if($LASTEXITCODE -ne 0){exit $LASTEXITCODE}
Write-Host 'Pipeline completo: PASS'
