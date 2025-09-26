# Hello World NiceGUI App

Eine einfache Hello World Anwendung erstellt mit [NiceGUI](https://nicegui.io/) - einem Python-Framework für moderne Web-Benutzeroberflächen.

## 🚀 Features

- **Interaktive Begrüßung**: Geben Sie Ihren Namen ein und erhalten Sie eine personalisierte Begrüßung
- **Moderne UI**: Sauberes, responsives Design mit NiceGUI
- **Hot-Reload**: Automatisches Neuladen bei Änderungen während der Entwicklung

## 📋 Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Installer)

## 🛠️ Installation

1. **Klonen Sie das Repository:**
   ```bash
   git clone https://github.com/rapdue/ep2_9.git
   cd ep2_9
   ```

2. **Virtuelle Umgebung erstellen (empfohlen):**
   ```bash
   python -m venv .venv
   ```

3. **Virtuelle Umgebung aktivieren:**
   
   **Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **Windows (CMD):**
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Verwendung

1. **Starten Sie die Anwendung:**
   ```bash
   python main.py
   ```

2. **Öffnen Sie Ihren Browser:**
   Die Anwendung öffnet automatisch http://localhost:8080

3. **Interagieren Sie mit der App:**
   - Geben Sie Ihren Namen in das Eingabefeld ein
   - Klicken Sie auf "Begrüßen"
   - Erkunden Sie die zusätzlichen Informationen

## 📁 Projektstruktur

```
ep2_9/
├── main.py              # Hauptanwendung
├── requirements.txt     # Python-Abhängigkeiten
├── README.md           # Projektdokumentation
└── .venv/              # Virtuelle Umgebung (lokal)
```

## 🔧 Entwicklung

Die Anwendung ist mit Hot-Reload konfiguriert. Änderungen an `main.py` werden automatisch übernommen, ohne die Anwendung neu starten zu müssen.

### Nützliche Befehle:

- **Abhängigkeiten aktualisieren:** `pip freeze > requirements.txt`
- **Port ändern:** Ändern Sie die `port`-Parameter in `main.py`
- **Debug-Modus:** Setzen Sie `show=False` in `ui.run()` zum Testen ohne Browser

## 📚 Weitere Ressourcen

- [NiceGUI Dokumentation](https://nicegui.io/)
- [NiceGUI Beispiele](https://github.com/zauberzeug/nicegui/tree/main/examples)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## 🌐 GitHub Pages Deployment

Dieses Projekt kann automatisch auf GitHub Pages veröffentlicht werden!

### Für öffentliche Repositories (kostenlos):
1. **Repository auf GitHub erstellen und pushen**
2. **GitHub Pages aktivieren:**
   - Gehe zu Repository Settings → Pages
   - Source: "GitHub Actions" auswählen
   - Die Workflow-Datei `.github/workflows/deploy.yml` wird automatisch erkannt

### Für private Repositories:
- Benötigt GitHub Pro, Team oder Enterprise Cloud
- Gleiche Schritte wie oben

### 🏗️ Build-Prozess:
```bash
# Lokaler Build-Test:
python build_static.py
```

Die statische Version wird automatisch bei jedem Push auf `main`/`master` erstellt und deployed.

### 📍 Live-Demo:
Nach dem Deployment ist die App verfügbar unter:
`https://rapdue.github.io/ep2_9/`

## 🤝 Mitwirken

1. Forken Sie das Projekt
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Pushen Sie zum Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie einen Pull Request

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz - siehe die [LICENSE](LICENSE) Datei für Details.

## 🏷️ Version

Aktuelle Version: 1.0.0