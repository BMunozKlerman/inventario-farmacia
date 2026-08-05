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
if(-not $codex){throw 'Codex CLI no está disponible. Instálalo e inicia sesión con tu cuenta ChatGPT.'}
& $codex.Source login status *> $null
if($LASTEXITCODE -ne 0){throw 'Codex CLI no tiene una sesión activa. Ejecuta: codex login'}
$renderer=Get-ChildItem (RepoPath 'tools/poppler') -Recurse -Filter pdftoppm.exe -File -ErrorAction SilentlyContinue|Select-Object -First 1
if(-not $renderer){$renderer=Get-Command pdftoppm -ErrorAction SilentlyContinue}
if(-not $renderer){throw 'Poppler no está disponible: falta pdftoppm.exe'}
$rendererExe=if($renderer.Source){$renderer.Source}else{$renderer.FullName}

$dirs=@('evidence','com','mapping','composed','audit')
foreach($d in $dirs){New-Item -ItemType Directory -Force (RepoPath $d)|Out-Null}
if(-not $KeepExisting){
  foreach($d in $dirs){
    $base=(RepoPath $d).TrimEnd('\')+'\'
    foreach($f in @(Get-ChildItem $base -Filter "$DeliveryId-*" -File -ErrorAction SilentlyContinue)){
      if(-not $f.FullName.StartsWith($base,[StringComparison]::OrdinalIgnoreCase)){throw 'Ruta de limpieza insegura'}
      Remove-Item -LiteralPath $f.FullName -Force
    }
  }
}

Write-Host '[1/5] Renderizando el PDF localmente'
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
@{delivery_id=$DeliveryId;source="resources/$([IO.Path]::GetFileName($pdf))";source_sha256=(Get-FileHash $pdf -Algorithm SHA256).Hash.ToLowerInvariant();pages=$pages}|ConvertTo-Json -Depth 10|Set-Content (Join-Path (RepoPath 'evidence') "$DeliveryId-page-index.json") -Encoding utf8
$images=@(Get-ChildItem (RepoPath 'evidence') -Filter "$DeliveryId-p*.png" -File|Sort-Object Name)

Write-Host '[2/5] Ejecutando las skills con Codex CLI y la licencia ChatGPT'
$mode=if($ComOnly){'Detente después de generar y validar conceptualmente los siete COM; no transformes ni compongas.'}else{'Después de los COM ejecuta 7cs-com-transform, 7cs-spec-compose y deja los artefactos para 7cs-spec-audit.'}
$prompt=@"
Procesa el delivery '$DeliveryId' usando exclusivamente las skills locales del repositorio y las imágenes adjuntas, que corresponden en orden al PDF resources/$([IO.Path]::GetFileName($pdf)).

Flujo obligatorio:
1. Lee y aplica `7cs-canvas-ingest` para el índice de páginas, pero no permitas que genere COM.
2. Entrega cada página a TODOS los lectores: `7cs-business-context`, `7cs-architectural-context`, `7cs-system-context`, `7cs-structural`, `7cs-functional-A`, `7cs-functional-B`, `7cs-deployment`.
3. Cada lector acepta sólo su canvas, ignora los demás y genera únicamente un COM literal bajo com/. No inventes texto ilegible ni derives requisitos dentro del COM.
4. El presupuesto esperado es exactamente un COM de cada tipo: business_context, architectural_context, system_context, structural, functional/front, functional/back y deployment.
5. Usa nombres `com/$DeliveryId-<canvas>[-<variant>]-p<N>.json` e ids estables según cada skill.
6. Actualiza `evidence/$DeliveryId-page-index.json` y crea `evidence/$DeliveryId-ingest-report.md`.
7. $mode
8. No modifiques resources/, .agents/, scripts/, config/, tests/, tools/, README.md ni AGENTS.md.

Trabaja hasta escribir los artefactos. Ante una discrepancia real usa NEEDS CLARIFICATION y no falsifiques evidencia.
"@
$args=@('exec','--ephemeral','--color','never','-s','workspace-write','-C',$root)
foreach($image in $images){$args+=@('-i',$image.FullName)}
$args+=$prompt
& $codex.Source @args
if($LASTEXITCODE -ne 0){throw "codex exec falló: $LASTEXITCODE"}

Write-Host '[3/5] Validando los COM presupuestados'
$budget=Get-Content -Raw (RepoPath $BudgetPath)|ConvertFrom-Json
$counts=@{business_context=0;architectural_context=0;system_context=0;structural=0;functional_front=0;functional_back=0;deployment=0}
$ids=@();$comFiles=@(Get-ChildItem (RepoPath 'com') -Filter "$DeliveryId-*.json" -File)
if(-not $comFiles){throw 'Codex no generó COM'}
foreach($file in $comFiles){
  $com=Get-Content -Raw $file.FullName|ConvertFrom-Json
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

if($ComOnly){Write-Host '[4/5] Transformación omitida';Write-Host '[5/5] PDF -> COM: PASS';exit 0}
Write-Host '[4/5] Ejecutando auditoría determinista'
& (Join-Path $PSScriptRoot 'audit-pipeline.ps1') -DeliveryId $DeliveryId
if($LASTEXITCODE -ne 0){exit $LASTEXITCODE}
Write-Host '[5/5] Pipeline completo: PASS'
