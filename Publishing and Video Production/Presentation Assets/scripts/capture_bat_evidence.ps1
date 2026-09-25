$ErrorActionPreference='Stop'
$assetRoot=Split-Path -Parent $PSScriptRoot
$src=Get-Content -Raw -LiteralPath (Join-Path $assetRoot 'content\source-material.json') | ConvertFrom-Json
$episode=$src.articles | Where-Object id -eq 'OE-VALUATION-06'
$sourceFile=$episode.evidence[0].workbook
$before=(Get-FileHash -LiteralPath $sourceFile -Algorithm SHA256).Hash.ToLower()
$excel=New-Object -ComObject Excel.Application
$excel.Visible=$false;$excel.DisplayAlerts=$false;$excel.AutomationSecurity=3
try {
 $book=$excel.Workbooks.Open($sourceFile,0,$true)
 try {
  $sheet=$book.Worksheets.Item('NSE Casebook')
  $sheet.PageSetup.PrintArea='C11:F11';$sheet.PageSetup.Orientation=2;$sheet.PageSetup.Zoom=$false
  $sheet.PageSetup.FitToPagesWide=1;$sheet.PageSetup.FitToPagesTall=1;$sheet.PageSetup.PrintHeadings=$true
  $sheet.PageSetup.PrintGridlines=$false;$sheet.PageSetup.CenterHorizontally=$true
  $sheet.PageSetup.LeftMargin=12;$sheet.PageSetup.RightMargin=12;$sheet.PageSetup.TopMargin=12;$sheet.PageSetup.BottomMargin=12
  $sheet.PageSetup.LeftHeader='';$sheet.PageSetup.CenterHeader='';$sheet.PageSetup.RightHeader=''
  $sheet.PageSetup.LeftFooter='';$sheet.PageSetup.CenterFooter='';$sheet.PageSetup.RightFooter=''
  $sheet.ExportAsFixedFormat(0,(Join-Path $assetRoot 'Evidence\Workbooks\OE-VALUATION-06-BAT.pdf'))
 } finally {$book.Close($false)}
} finally {$excel.Quit();[void][Runtime.InteropServices.Marshal]::ReleaseComObject($excel)}
$after=(Get-FileHash -LiteralPath $sourceFile -Algorithm SHA256).Hash.ToLower()
if($before -ne $after){throw 'Source hash changed'}
@{episode='OE-VALUATION-06';asset_id='OE-VALUATION-06-BAT';workbook=$sourceFile;sheet='NSE Casebook';range='C11:F11';sha256=$after;method='Microsoft Excel read-only PDF range export. Print headings retained. Source not saved.';bridge=$false;scope='BAT Kenya FY2025 net revenue rounded to KES 23.192bn. OCF deliberately outside this crop because the article/workbook source-line reconciliation is unresolved.'} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $assetRoot 'Evidence\Workbooks\bat-capture-manifest.json') -Encoding utf8
Write-Output 'BAT evidence captured; source SHA-256 unchanged.'
