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
   git clone https://github.com/rapdue/test-nice-gui.git
   cd test-nice-gui
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

## 🌍 Live (echter) NiceGUI Server starten

Standard `main.py` startet schon den Entwicklungsserver mit Hot-Reload.
Für Produktionsbetrieb ohne Reload und ohne automatisches Browser-Öffnen kannst du `serve.py` verwenden:

```bash
python serve.py
```

Dieser nutzt `host=0.0.0.0`, damit er auch in Containern erreichbar ist.

### Docker Build & Run

```bash
docker build -t test-nice-gui .
docker run -p 8080:8080 test-nice-gui
```
Dann aufrufen: http://localhost:8080

### Plattformen
- Render / Railway / Fly.io: Dockerfile direkt verwenden
- Heroku kompatibel: `Procfile` vorhanden (`web: python serve.py`)
- Azure / AWS ECS: Port 8080 freigeben

## ☁️ Deployment auf Render

Schnellstart (ohne Änderungen):
1. Push sicherstellen (Repo aktuell auf GitHub)
2. Gehe zu https://dashboard.render.com
3. New + → Web Service
4. Repository auswählen
5. Einstellungen:
   - Environment: Python
   - Build Command: `pip install --upgrade pip && pip install -r requirements.txt`
   - Start Command: `python serve.py`
   - Region: nahe bei dir
6. Create Web Service
7. Warten bis Build fertig → Live-URL kopieren

Mit `render.yaml` (Infrastructure as Code):
1. In Render: New + → Blueprint → GitHub Repo wählen
2. Deploy → Render liest `render.yaml`
3. Live deployment nach jedem Push

### Health Check
Standard `healthCheckPath: /` funktioniert (Root liefert HTML). Falls leer, einfach ein kleines Element oben belassen.

### Logs ansehen
Render Dashboard → Service → Logs

### Environment Variablen
Kannst du in Render UI überschreiben (PORT, DEBUG, etc.).

### Custom Domain
Render Dashboard → Service → Custom Domains → Domain hinzufügen und DNS A/CNAME setzen.

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
`https://rapdue.github.io/test-nice-gui/`

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