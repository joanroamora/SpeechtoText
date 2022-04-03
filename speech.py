import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    
    print("Di lo que quieras llevar a texto, de manera pausada y clara por favor: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='es-ES')
        print("Lo que has dicho es lo siguiente: {}".format(text))
    except:
        print("Lo siento, no te entendi!")