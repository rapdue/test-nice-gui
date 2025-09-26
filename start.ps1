# Hello World NiceGUI App Starter
# Dieses Script startet die NiceGUI Anwendung

Write-Host "🚀 Starte Hello World NiceGUI App..." -ForegroundColor Green
Write-Host ""
Write-Host "📍 Die App wird verfügbar sein auf:" -ForegroundColor Yellow
Write-Host "   http://localhost:8080" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 Drücken Sie Ctrl+C um die App zu beenden" -ForegroundColor Gray
Write-Host ""

# Wechsle zum Script-Verzeichnis
Set-Location $PSScriptRoot

# Starte die Python-Anwendung
& ".\.venv\Scripts\python.exe" main.py

# Warte auf Benutzereingabe nach Beendigung
Write-Host ""
Write-Host "App wurde beendet. Drücken Sie eine beliebige Taste..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")