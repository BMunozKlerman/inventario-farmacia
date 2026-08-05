[CmdletBinding()]
param(
  [string]$PdfPath,
  [ValidatePattern('^[A-Za-z0-9_-]+$')][string]$DeliveryId = 'E1',
  [switch]$ComOnly
)

$ErrorActionPreference='Stop'
$root=[IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))

if(-not $PdfPath){
  $pdfs=@(Get-ChildItem (Join-Path $root 'resources') -Filter '*.pdf' -File)
  if($pdfs.Count -eq 0){throw 'No hay ningún PDF en resources/.'}
  if($pdfs.Count -gt 1){throw 'Hay más de un PDF en resources/. Indica uno con: .\run-project.cmd -PdfPath ".\resources\archivo.pdf"'}
  $PdfPath=$pdfs[0].FullName
}

$pipelineArgs=@{
  PdfPath=$PdfPath
  DeliveryId=$DeliveryId
}
if($ComOnly){$pipelineArgs.ComOnly=$true}

& (Join-Path $PSScriptRoot 'run-pipeline.ps1') @pipelineArgs
exit $LASTEXITCODE
