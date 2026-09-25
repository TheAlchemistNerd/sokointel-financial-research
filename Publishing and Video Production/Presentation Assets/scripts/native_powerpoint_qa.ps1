param([string[]]$EpisodeIds=@(),[switch]$Render,[switch]$RenderRepresentatives)
$ErrorActionPreference='Stop'
$assetRoot=Split-Path -Parent $PSScriptRoot
$manifest=Get-Content -Raw -LiteralPath (Join-Path $assetRoot 'episode-manifest.json') | ConvertFrom-Json
$qa=@()
$ppt=New-Object -ComObject PowerPoint.Application
try {
 foreach($episode in $manifest.episodes) {
  if($EpisodeIds.Count -gt 0 -and $episode.article_id -notin $EpisodeIds) {continue}
  $deckPath=[IO.Path]::GetFullPath((Join-Path $assetRoot $episode.path)).Replace('/','\')
  $presentation=$ppt.Presentations.Open($deckPath,$true,$false,$false)
  try {
   $issues=@()
   foreach($slide in $presentation.Slides) {
    foreach($shape in $slide.Shapes) {
     if($shape.HasTextFrame -and $shape.TextFrame.HasText) {
      $text=$shape.TextFrame.TextRange.Text
      $boundHeight=$shape.TextFrame.TextRange.BoundHeight
      $boundWidth=$shape.TextFrame.TextRange.BoundWidth
      $boundTop=$shape.TextFrame.TextRange.BoundTop
      $boundLeft=$shape.TextFrame.TextRange.BoundLeft
      if(($boundTop+$boundHeight) -gt 501 -and $shape.Top -lt 490) {
       $issues+=@{slide=$slide.SlideIndex;kind='body-near-footer';text=$text;top=$boundTop;height=$boundHeight;shape_height=$shape.Height}
      }
      if($boundHeight -gt ($shape.Height+5) -and $shape.Top -lt 490) {
       $issues+=@{slide=$slide.SlideIndex;kind='text-exceeds-box';text=$text;top=$boundTop;height=$boundHeight;shape_height=$shape.Height}
      }
      if(($boundLeft+$boundWidth) -gt 955) {
       $issues+=@{slide=$slide.SlideIndex;kind='text-right-edge';text=$text;left=$boundLeft;width=$boundWidth}
      }
     }
    }
   }
   $renderThis=$Render -or ($RenderRepresentatives -and $episode.article_id -in @('AMBC-02','IIDF-03','KTHF-03','KECA-02','NSE-DG-01','USMPC-09','LEAD-01','OE-MSME-01','OE-VALUATION-09','OE-FAILURE-12','STARTUP-FUNDING-02'))
   if($renderThis) {
    $renderDir=Join-Path $assetRoot ('Review\Native\'+$episode.article_id)
    New-Item -ItemType Directory -Force -Path $renderDir | Out-Null
    $presentation.Export($renderDir,'PNG',1600,900)
   }
   $qa+=@{article_id=$episode.article_id;slides=$presentation.Slides.Count;issues=$issues;rendered=[bool]$renderThis;sha256=(Get-FileHash -LiteralPath $deckPath -Algorithm SHA256).Hash.ToLower()}
   Write-Output ($episode.article_id+' native-opened; '+$issues.Count+' potential text issues')
  } finally { $presentation.Close() }
 }
} finally { [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($ppt) }
$dest=Join-Path $assetRoot ('Review\native-qa'+$(if($EpisodeIds.Count -gt 0){'-selected'}else{''})+'.json')
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dest) | Out-Null
$qa | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $dest -Encoding utf8
if($EpisodeIds.Count -gt 0) {
 $fullPath=Join-Path $assetRoot 'Review\native-qa.json'
 $previous=if(Test-Path -LiteralPath $fullPath){@(Get-Content -Raw -LiteralPath $fullPath | ConvertFrom-Json)}else{@()}
 $merged=@($previous | Where-Object {$_.article_id -notin $EpisodeIds})+@($qa)
 $merged | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $fullPath -Encoding utf8
}
Write-Output $dest
