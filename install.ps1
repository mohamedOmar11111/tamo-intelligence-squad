# TAMO INTELLIGENCE SQUAD - WINDOWS INSTALLER v1.0.0

Write-Host "------------------------------------------------" -ForegroundColor Cyan
Write-Host "  TAMO INTELLIGENCE SQUAD - INSTALLER" -ForegroundColor Cyan
Write-Host "------------------------------------------------" -ForegroundColor Cyan

# 1. Environment Setup
Write-Host "> Initializing TAMO Kernel..." -ForegroundColor White
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install rich requests exa-py firecrawl-py python-dotenv --quiet

# 2. Alias Configuration (PowerShell Profile)
Write-Host "> Injecting TAMO Alias..." -ForegroundColor White
$ProfilePath = $PROFILE
if (!(Test-Path $ProfilePath)) {
    New-Item -Type File -Path $ProfilePath -Force
}

$CurrentDir = Get-Location
$AliasLine = "function tamo { python '$CurrentDir\kernel\cli.py' `$args }"
Add-Content -Path $ProfilePath -Value "`n$AliasLine"

# 3. Finalizing
Write-Host "------------------------------------------------" -ForegroundColor Green
Write-Host "  INSTALLATION COMPLETE" -ForegroundColor Green
Write-Host "  Restart your terminal and type 'tamo' to start." -ForegroundColor White
Write-Host "------------------------------------------------" -ForegroundColor Green
