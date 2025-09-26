#!/usr/bin/env python3
"""
Hello World NiceGUI Application
Eine einfache Web-App mit NiceGUI
"""

from nicegui import ui


def main():
    """Hauptfunktion der NiceGUI Anwendung"""
    
    # Seitentitel setzen
    ui.page_title('Hello World - NiceGUI')
    
    # Header
    with ui.header(elevated=True).style('background-color: #3874cb').classes('items-center justify-between'):
        ui.label('Hello World App').classes('text-h6')
    
    # Hauptinhalt
    with ui.column().classes('w-full max-w-md mx-auto mt-8 p-4'):
        # Titel
        ui.label('🌍 Hello World!').classes('text-h3 text-center mb-4')
        
        # Beschreibungstext
        ui.label('Willkommen zu Ihrer ersten NiceGUI Anwendung!').classes('text-center mb-6')
        
        # Interaktives Element - Eingabefeld
        name_input = ui.input('Ihr Name:', placeholder='Geben Sie Ihren Namen ein...')
        
        # Label für die Begrüßung
        greeting_label = ui.label('')
        
        # Button zum Begrüßen
        def greet():
            if name_input.value:
                greeting_label.text = f'Hallo {name_input.value}! 👋'
                greeting_label.classes('text-h5 text-center text-green-600 mt-4')
            else:
                greeting_label.text = 'Bitte geben Sie Ihren Namen ein!'
                greeting_label.classes('text-center text-red-500 mt-4')
        
        ui.button('Begrüßen', on_click=greet).classes('w-full mt-4')
        
        # Zusätzliche Informationen
        with ui.expansion('Mehr Informationen', icon='info').classes('w-full mt-6'):
            ui.label('Diese App wurde mit NiceGUI erstellt - einem Python-Framework für Web-Interfaces.')
            ui.label('NiceGUI macht es einfach, moderne Web-Apps mit Python zu entwickeln!')
        
        # Footer
        with ui.card().classes('w-full mt-8 p-4'):
            ui.label('📚 Nächste Schritte:')
            ui.label('• Erkunden Sie die NiceGUI Dokumentation')
            ui.label('• Fügen Sie weitere UI-Elemente hinzu')
            ui.label('• Erweitern Sie die Funktionalität')


if __name__ in {'__main__', '__mp_main__'}:
    # WICHTIG: main() aufrufen damit Elemente erstellt werden
    main()
    print('Starte NiceGUI Server auf http://localhost:8080 ...')
    # Starte die NiceGUI Anwendung
    ui.run(
        title='Hello World NiceGUI',
        port=8080,
        show=True,  # Öffnet automatisch den Browser
        reload=True  # Aktiviert Hot-Reload für Entwicklung
    )