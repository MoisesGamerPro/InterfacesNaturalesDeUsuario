import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

print("speak:")
with mic as source:
    print("Ajustando")
    r.adjust_for_ambient_noise(source)
    print("Escuchando")
    audio = r.listen(source)

try:
    print("Enviando a google...")
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("No entiendo, habla mas fuerte!")
except sr.RequestError as e:
    print("Sphinx error ; {0}".format(e)) 