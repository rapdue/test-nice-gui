@echo off
echo Starte Hello World NiceGUI App...
echo.
echo Die App wird auf http://localhost:8080 verfügbar sein
echo Drücken Sie Ctrl+C um die App zu beenden
echo.

cd /d "%~dp0"
".\.venv\Scripts\python.exe" main.py

pause