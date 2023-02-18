
import pyttsx3 as voz
import speech_recognition as sr
import subprocess as sub
import webbrowser
from datetime import datetime

voice = voz.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[2].id)
voice.setProperty('rate' ,140)

decision = bool(True)

def say(text):
    voice.say(text)
    voice.runAndWait()
    
while decision == (True):
    recognizer=sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Escuchando...')
        audio=recognizer.listen(source, phrase_time_limit=3)
        
    try:
        comando=recognizer.recognize_google(audio, language='es-MX')
        print(f'Creo que dijiste "{comando}"')
        
        comando=comando.lower()
        comando=comando.split(' ')
        
        if 'alexa' in comando:

                if 'abre' in comando or 'abrir' in comando:
                
                    sites={
                        'google':'google.com',
                        'youtube':'youtube.com',
                        'ubicación': 'maps.google.es',
                        'wikipedia': 'wikipedia.org '
                    }

                    for i in list(sites.keys()):
                        if i in comando:
                            sub.call(f'start msedge.exe {sites[i]}', shell=True)
                            say(f'Abriendo {i}')
                        
                elif 'hora' in comando:
                    time=datetime.now().strftime('%H:%M')
                    say(f'Son las {time}')  
                    
                elif 'hola' in comando:
                    say('hola como estas!')

                elif 'cartman' in comando:
                    say('XD')

                elif 'tusa' in comando:
                   webbrowser.open('https://www.youtube.com/watch?v=tbneQDc2H3I')

                elif 'repositorio' in comando:
                   webbrowser.open('https://github.com/mfbr352/IA')

                for i in ['termina', 'terminar', 'finaliza','finalizó','finalizado']:
                    if i in comando:
                        say('Sesion finalizada')
                        decision = bool(False)
                        break
    except:
        print('No te entendi que dijiste, por favor vuelve a intentarlo')