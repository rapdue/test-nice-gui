# 🚀 GitHub Pages Setup Anleitung

## Schritt-für-Schritt Anleitung für GitHub Pages Deployment

### 📋 Voraussetzungen

**Für öffentliche Repositories:** ✅ Kostenlos verfügbar  
**Für private Repositories:** Benötigt GitHub Pro/Team/Enterprise Cloud

### 🔧 Setup-Schritte

#### 1. Repository auf GitHub erstellen

1. Gehe zu [GitHub.com](https://github.com) und logge dich ein
2. Klicke auf "New Repository" (grüner Button)
3. Repository-Name: `test-nice-gui`
4. Beschreibung: `Hello World NiceGUI Web App`
5. Wähle "Private" oder "Public" je nach Bedarf
6. **Wichtig:** Haken Sie NICHT an:
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license
7. Klicke "Create repository"

#### 2. Lokales Repository mit GitHub verbinden

```powershell
# In Ihrem Projektordner (bereits erledigt):
cd "C:/Users/RaphaelDütsch/OneDrive - abrantix AG/projects/ep2_9"

# Remote-Repository hinzufügen:
git remote add origin https://github.com/rapdue/test-nice-gui.git

# Optional: Branch umbenennen zu 'main' (falls gewünscht):
git branch -M main

# Dateien zu GitHub pushen:
git push -u origin master
# oder falls Sie zu 'main' umbenannt haben:
# git push -u origin main
```

#### 3. GitHub Pages aktivieren

1. Gehe zu Ihrem Repository auf GitHub
2. Klicke auf **"Settings"** (Tab oben rechts)
3. Scrolle runter zu **"Pages"** (linke Seitenleiste)
4. Bei **"Source"** wählen Sie: **"GitHub Actions"**
5. Die Workflow-Datei `.github/workflows/deploy.yml` wird automatisch erkannt
6. Klicke **"Save"**

#### 4. Erste Deployment auslösen

```powershell
# Kleiner Commit um Deployment zu triggern:
git commit --allow-empty -m "Trigger first GitHub Pages deployment"
git push
```

#### 5. Deployment Status prüfen

1. Gehe zu **"Actions"** Tab in Ihrem Repository
2. Sie sollten einen laufenden Workflow sehen: "Deploy NiceGUI to GitHub Pages"
3. Klicken Sie auf den Workflow um Details zu sehen
4. Nach erfolgreichem Deployment (grüner Haken ✅):

### 🌐 Ihre Live-Website

Nach erfolgreichem Deployment ist Ihre App verfügbar unter:
```
https://rapdue.github.io/test-nice-gui/
```

### 🔄 Automatische Updates

- **Automatisch:** Jeder Push auf `master`/`main` triggert ein neues Deployment
- **Build-Zeit:** Normalerweise 2-5 Minuten
- **Status:** Sichtbar im "Actions" Tab

### 🛠️ Lokales Testen der statischen Version

```powershell
# Build-Script ausführen:
python build_static.py

# Inhalt des dist-Ordners prüfen:
ls dist/

# Optional: Lokaler HTTP-Server zum Testen:
cd dist
python -m http.server 8000
# Dann öffnen: http://localhost:8000
```

### 📧 Benachrichtigungen

GitHub sendet E-Mails bei:
- ✅ Erfolgreichem Deployment
- ❌ Fehlern beim Deployment

### 🚨 Troubleshooting

#### Problem: Workflow schlägt fehl
- Gehe zu "Actions" Tab und klicke auf den fehlgeschlagenen Workflow
- Prüfe die Logs für Fehlermeldungen
- Häufige Ursachen:
  - Syntax-Fehler in `deploy.yml`
  - Python-Abhängigkeiten fehlen
  - Permissions nicht korrekt

#### Problem: Seite ist nicht erreichbar
- Prüfe Repository Settings → Pages
- Stelle sicher, dass "GitHub Actions" als Source gewählt ist
- Warte bis zu 10 Minuten nach dem Deployment

#### Problem: Private Repository ohne GitHub Pages
- Upgrade auf GitHub Pro ($4/Monat)
- Oder Repository auf "Public" umstellen (kostenlos)

### 🎯 Nächste Schritte

Nach erfolgreichem Setup können Sie:
1. **Custom Domain:** Eigene Domain mit GitHub Pages verbinden
2. **SSL-Zertifikat:** Automatisch durch GitHub bereitgestellt
3. **Analytics:** Google Analytics oder andere Tools hinzufügen
4. **SEO:** Meta-Tags und OpenGraph-Tags optimieren

### 📞 Support

- **GitHub Docs:** [GitHub Pages Documentation](https://docs.github.com/en/pages)
- **NiceGUI Docs:** [nicegui.io](https://nicegui.io/)
- **Issues:** Erstellen Sie ein Issue in diesem Repository