#!/usr/bin/env python3
"""
Build Script für GitHub Pages Deployment
Erstellt eine statische Version der NiceGUI App
"""

import os
import shutil
from pathlib import Path

def build_static():
    """Erstellt eine statische Version für GitHub Pages"""
    
    # Dist-Ordner erstellen
    dist_dir = Path("dist")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # HTML-Template für die statische Seite
    html_content = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World NiceGUI - Demo</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: white;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 2.5em;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        .demo-section {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }
        .input-group {
            margin: 15px 0;
        }
        .input-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .input-group input {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            box-sizing: border-box;
        }
        .btn {
            background: #4CAF50;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px 5px;
            transition: background 0.3s;
        }
        .btn:hover {
            background: #45a049;
        }
        .greeting {
            margin: 20px 0;
            padding: 15px;
            background: rgba(76, 175, 80, 0.3);
            border-radius: 5px;
            min-height: 20px;
            font-size: 1.2em;
            text-align: center;
        }
        .info-box {
            background: rgba(33, 150, 243, 0.3);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }
        .github-link {
            display: inline-block;
            background: #333;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 5px;
            transition: background 0.3s;
        }
        .github-link:hover {
            background: #555;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌍 Hello World NiceGUI</h1>
            <p>Eine Demo der NiceGUI Python Web-App</p>
        </div>
        
        <div class="demo-section">
            <h2>🚀 Interaktive Demo</h2>
            <p>Diese statische Version simuliert die NiceGUI-App:</p>
            
            <div class="input-group">
                <label for="nameInput">Ihr Name:</label>
                <input type="text" id="nameInput" placeholder="Geben Sie Ihren Namen ein...">
            </div>
            
            <button class="btn" onclick="greetUser()">Begrüßen</button>
            <button class="btn" onclick="clearGreeting()">Zurücksetzen</button>
            
            <div class="greeting" id="greeting">
                Geben Sie Ihren Namen ein und klicken Sie auf "Begrüßen"!
            </div>
        </div>
        
        <div class="info-box">
            <h3>📚 Über dieses Projekt</h3>
            <p><strong>NiceGUI</strong> ist ein Python-Framework für moderne Web-Benutzeroberflächen.</p>
            <p>Diese Demo zeigt eine einfache "Hello World" Anwendung mit:</p>
            <ul>
                <li>✅ Interaktiver Benutzereingabe</li>
                <li>✅ Moderner, responsiver UI</li>
                <li>✅ Python-Backend mit NiceGUI</li>
                <li>✅ Automatischem Browser-Opening</li>
                <li>✅ Hot-Reload für Entwicklung</li>
            </ul>
        </div>
        
        <div class="info-box">
            <h3>🔧 Lokale Installation & Verwendung</h3>
            <p>Um die echte NiceGUI-App lokal zu starten:</p>
            <pre style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 5px; overflow-x: auto;">
git clone https://github.com/ihr-username/ep2_9.git
cd ep2_9
python -m venv .venv
.venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
python main.py</pre>
            <p>Die App wird dann auf <code>http://localhost:8080</code> verfügbar sein.</p>
        </div>
        
        <div style="text-align: center; margin: 20px 0;">
            <a href="https://github.com/ihr-username/ep2_9" class="github-link">
                📂 Projekt auf GitHub ansehen
            </a>
            <a href="https://nicegui.io/" class="github-link">
                📖 NiceGUI Dokumentation
            </a>
        </div>
        
        <div class="footer">
            <p>Erstellt mit ❤️ und <a href="https://nicegui.io/" style="color: #fff;">NiceGUI</a></p>
            <p>© 2025 - Hello World NiceGUI Demo</p>
        </div>
    </div>

    <script>
        function greetUser() {
            const nameInput = document.getElementById('nameInput');
            const greeting = document.getElementById('greeting');
            const name = nameInput.value.trim();
            
            if (name) {
                greeting.innerHTML = `Hallo <strong>${name}</strong>! 👋<br><small>In der echten NiceGUI-App wäre das noch interaktiver!</small>`;
                greeting.style.background = 'rgba(76, 175, 80, 0.5)';
            } else {
                greeting.innerHTML = '❌ Bitte geben Sie Ihren Namen ein!';
                greeting.style.background = 'rgba(244, 67, 54, 0.5)';
            }
        }
        
        function clearGreeting() {
            document.getElementById('nameInput').value = '';
            const greeting = document.getElementById('greeting');
            greeting.innerHTML = 'Geben Sie Ihren Namen ein und klicken Sie auf "Begrüßen"!';
            greeting.style.background = 'rgba(33, 150, 243, 0.3)';
        }
        
        // Enter-Taste unterstützung
        document.getElementById('nameInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                greetUser();
            }
        });
        
        // Animationseffekt beim Laden
        window.addEventListener('load', function() {
            document.querySelector('.container').style.animation = 'fadeIn 0.5s ease-in';
        });
    </script>
    
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</body>
</html>"""
    
    # HTML-Datei schreiben
    (dist_dir / "index.html").write_text(html_content, encoding='utf-8')
    
    # README für GitHub Pages erstellen
    readme_content = """# Hello World NiceGUI - GitHub Pages Demo

Diese Seite zeigt eine statische Demo der NiceGUI Hello World Anwendung.

## 🌐 Live Demo
[Hier ansehen](https://ihr-username.github.io/ep2_9/)

## 📁 Originales Repository
Das vollständige NiceGUI-Projekt finden Sie im [Haupt-Repository](https://github.com/ihr-username/ep2_9).

## 🚀 Lokale Installation
Siehe die Anweisungen auf der Demo-Seite oder im Haupt-Repository.
"""
    
    (dist_dir / "README.md").write_text(readme_content, encoding='utf-8')
    
    print("✅ Statische Seite wurde erfolgreich in ./dist/ erstellt!")
    print("📁 Dateien:")
    for file in dist_dir.iterdir():
        print(f"   - {file.name}")

if __name__ == "__main__":
    build_static()