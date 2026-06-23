$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    if (-not $content.Contains('rel="icon"')) {
        $content = $content -replace '(<title>.*?</title>)', "`$1`n    <link rel=`"icon`" href=`"favicon.svg`" type=`"image/svg+xml`">"
        [System.IO.File]::WriteAllText($file.FullName, $content)
        Write-Host "Added favicon to $($file.Name)"
    }
}
