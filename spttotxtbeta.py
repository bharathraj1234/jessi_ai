import speech_recognition as sr
import time
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:
            print("say something")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print("this is the text u talked   "+text)
            if "stop" in text or "exit" in text:
                print("Stopping the program")
                break
    except:
        print("u should say something ")
        r = sr.Recognizer()
        continue