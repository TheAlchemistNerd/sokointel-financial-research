param([Parameter(Mandatory=$true)][string]$DocumentPath,[Parameter(Mandatory=$true)][string]$PdfPath)
$ErrorActionPreference='Stop'
$editionApp=$null
$editionDoc=$null
try {
    $editionApp=New-Object -ComObject Word.Application
    $editionApp.Visible=$false
    $editionApp.DisplayAlerts=0
    $editionApp.AutomationSecurity=3
    $editionDoc=$editionApp.Documents.Open($DocumentPath,$false,$false,$false)
    foreach ($toc in $editionDoc.TablesOfContents) { $toc.Update() }
    $editionDoc.Fields.Update() | Out-Null
    $editionDoc.Repaginate()
    foreach ($toc in $editionDoc.TablesOfContents) { $toc.UpdatePageNumbers() }
    $editionDoc.Save()
    $editionDoc.ExportAsFixedFormat($PdfPath,17,$false,0,0,1,1,0,$true,$true,1,$true,$true,$false)
} finally {
    if ($null -ne $editionDoc) { $editionDoc.Close(0); [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($editionDoc) }
    if ($null -ne $editionApp) { $editionApp.Quit(); [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($editionApp) }
}
