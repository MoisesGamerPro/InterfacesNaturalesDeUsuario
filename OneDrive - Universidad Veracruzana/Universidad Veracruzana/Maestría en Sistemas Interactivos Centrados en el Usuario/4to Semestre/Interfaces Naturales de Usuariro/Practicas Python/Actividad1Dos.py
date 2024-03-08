import speech_recognition as sr
import nltk
from nltk import CFG

if not nltk.download('punkt'):
    print("No se pudo descargar el recurso punkt, asegúrate de tener conexión a internet")
    exit()

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Ajustando al ruido de fondo...")
    r.adjust_for_ambient_noise(source)

print("Dime algo:")
with mic as source:
    audio = r.listen(source)

try:
    reconocida_habla = r.recognize_google(audio, language='es-ES')
    print("Reconoció: " + reconocida_habla)

    tokens = nltk.word_tokenize(reconocida_habla)

#Gramática
    gramatica = nltk.CFG.fromstring("""
    O -> Reproduce Objeto
    Reproduce -> "Reproduce" | "Pon" | "Echame"
    Objeto -> Canción | Artista
    Cancion -> "de" | "la" 
    Artista -> "Jose Jose" | "Luis Miguel" | "Pepe Aguilar"
""")

    rd_parser = nltk.RecursiveDescentParser(gramatica)
    for tree in rd_parser.parse(tokens):
        print(tree)
        tree.pretty_print()

except sr.UnknownValueError:
    print("No entendí, habla más fuerte!")
except sr.RequestError as e:
    print("Sphinx error: {0}".format(e))
except ValueError:
    print("No se reconoce como oración del lenguaje")

from gtts import gTTS
import os

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='es')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

if __name__ == "__main__":
    speak('Escuché: ' + reconocida_habla)

import pywhatkit

# Reproducir un vídeo en YouTube
pywhatkit.playonyt(reconocida_habla)
speak('Reproduciendo en YouTube: ' + reconocida_habla)
