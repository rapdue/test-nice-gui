# 🔧 GitHub Pages Troubleshooting

## 🚨 Häufige Probleme und Lösungen

### Problem: "Failed to deploy to github-pages"

#### ✅ **Lösung 1: Repository Settings überprüfen**

1. Gehe zu **Repository Settings** → **Pages**
2. Stelle sicher, dass **Source** auf "**GitHub Actions**" gesetzt ist
3. **NICHT** "Deploy from a branch" wählen

#### ✅ **Lösung 2: Permissions überprüfen**

1. Gehe zu **Repository Settings** → **Actions** → **General**
2. Scrolle zu **"Workflow permissions"**
3. Wähle **"Read and write permissions"**
4. Aktiviere **"Allow GitHub Actions to create and approve pull requests"**

#### ✅ **Lösung 3: Environment überprüfen**

1. Gehe zu **Repository Settings** → **Environments**
2. Falls kein "**github-pages**" Environment existiert:
   - Klicke **"New environment"**
   - Name: `github-pages`
   - Keine besonderen Rules nötig

#### ✅ **Lösung 4: Manueller Workflow-Trigger**

1. Gehe zu **Actions** Tab
2. Wähle "**GitHub Pages**" Workflow
3. Klicke **"Run workflow"** → **"Run workflow"**

### 🔍 **Debug-Schritte:**

#### 1. Workflow-Logs überprüfen:
```
Actions Tab → Fehlgeschlagener Workflow → Job anklicken → Logs lesen
```

#### 2. Häufige Fehlermeldungen:

**"Error: Process completed with exit code 1"**
- Build-Script schlägt fehl
- Python-Dependencies fehlen
- Lösung: Lokales Testen mit `python build_static.py`

**"Error: Unable to download artifact"**
- Upload-Schritt fehlgeschlagen  
- Lösung: `./dist` Ordner wird nicht erstellt
- Check: Build-Script erzeugt `dist/` Ordner?

**"Error: Resource not accessible by integration"**
- Permissions-Problem
- Lösung: Repository Settings → Actions → Write permissions

#### 3. Lokales Testen:

```bash
# 1. Build testen
python build_static.py
ls dist/  # Sollte index.html, .nojekyll, README.md zeigen

# 2. Lokaler Server (optional)
cd dist
python -m http.server 8000
# Öffne: http://localhost:8000
```

### 🚀 **Alternative Deployment-Methoden:**

#### **Option A: Einfacher Static HTML Workflow**
Falls der Python-Build fehlschlägt, können Sie auch nur statische Dateien deployen:

1. Führe lokal aus: `python build_static.py`  
2. Committe den `dist/` Ordner
3. Nutze GitHub's "Static HTML" Workflow
4. Source Folder: `/dist`

#### **Option B: Manual Upload**
1. Baue lokal: `python build_static.py`
2. Zip den `dist/` Ordner  
3. GitHub Release erstellen mit dem Zip
4. GitHub Pages auf "Release" umstellen

### 📋 **Checkliste für funktionierendes Deployment:**

- ✅ Repository ist **Public** ODER GitHub Pro für Private
- ✅ **Settings** → **Pages** → **Source**: "GitHub Actions"  
- ✅ **Settings** → **Actions** → **Permissions**: "Read and write"
- ✅ Workflow-Datei in `.github/workflows/` vorhanden
- ✅ `build_static.py` funktioniert lokal
- ✅ `requirements.txt` enthält `nicegui`
- ✅ Kein `pull_request` Trigger im Workflow

### 🆘 **Wenn nichts funktioniert:**

1. **Deaktiviere GitHub Pages** (Settings → Pages → Source: None)
2. **Warte 5 Minuten**  
3. **Aktiviere erneut** (Source: GitHub Actions)
4. **Push einen neuen Commit** um Workflow auszulösen

### 📞 **Support-Ressourcen:**

- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [GitHub Actions Docs](https://docs.github.com/en/actions)  
- [Repository Issues](https://github.com/rapdue/test-nice-gui/issues)

---

**Falls der Fehler weiterhin besteht, teilen Sie bitte die genaue Fehlermeldung aus den Action-Logs mit!**