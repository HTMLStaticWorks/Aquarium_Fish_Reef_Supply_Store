$files = Get-ChildItem -Filter *.html

$mobileButtonsHtml = @"
                <div class="mobile-toggles mt-auto pt-4 border-top border-secondary d-flex justify-content-center gap-3">
                    <button class="theme-btn theme-toggle btn btn-outline-secondary rounded-circle" style="width: 50px; height: 50px;"><i class="bi bi-sun-fill"></i></button>
                    <button class="rtl-btn rtl-toggle btn btn-outline-secondary rounded-circle" style="width: 50px; height: 50px;"><i class="bi bi-arrow-left-right"></i></button>
                </div>
"@

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    
    $content = $content -replace '<button class="theme-btn" id="theme-toggle"><i class="bi bi-sun-fill"></i></button>', '<button class="theme-btn header-controls-btn theme-toggle" id="theme-toggle"><i class="bi bi-sun-fill"></i></button>'
    $content = $content -replace '<button class="rtl-btn" id="rtl-toggle"><i class="bi bi-arrow-left-right"></i></button>', '<button class="rtl-btn header-controls-btn rtl-toggle" id="rtl-toggle"><i class="bi bi-arrow-left-right"></i></button>'

    if (-not $content.Contains('class="mobile-toggles"')) {
        $content = $content -replace '(<a[^>]*href="login\.html"[^>]*>Login</a>)', "`$1`n$mobileButtonsHtml"
    }

    [System.IO.File]::WriteAllText($file.FullName, $content)
    Write-Host "Fixed $($file.Name)"
}
