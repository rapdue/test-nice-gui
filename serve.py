"""Production entrypoint for running the live NiceGUI server.
This starts the real Python NiceGUI backend (nicht die statische Demo).

Usage Beispiele:
  python serve.py                 # nutzt Port 8080 (Default)
  python serve.py --port 9090     # eigener Port per Argument
  $env:PORT=9001; python serve.py # PowerShell: PORT Umgebungsvariable
  PORT=9002 python serve.py       # Bash / Linux / macOS

Reihenfolge der Port-Ermittlung:
1. CLI Argument --port
2. Umgebungsvariable PORT
3. Default 8080
"""
from __future__ import annotations
import os
import argparse
from nicegui import ui

# Import the UI construction function from main.py
from main import main as build_ui  # type: ignore

# Build UI elements (same as local development)
build_ui()

def resolve_port() -> int:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--port', type=int, help='Port für den Server (überschreibt ENV PORT)')
    args = parser.parse_args()
    if args.port:
        return args.port
    env_port = os.getenv('PORT')
    if env_port and env_port.isdigit():
        return int(env_port)
    return 8080

if __name__ == '__main__':
    port = resolve_port()
    print(f'Starte NiceGUI Produktions-Server auf Port {port} (http://localhost:{port})')
    print('Hinweis: Falls Port belegt ist: Prozess finden mit:')
    print('  PowerShell:  Get-NetTCPConnection -LocalPort {0} | Select-Object -Property OwningProcess'.format(port))
    print('  Dann:        Stop-Process -Id <PID>')
    ui.run(
        title='Hello World NiceGUI',
        host='0.0.0.0',
        port=port,
        show=False,       # On a server we don't want to open a browser
        reload=False      # Disable auto-reload in production
    )
