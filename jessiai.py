import speech_recognition as sr
import os
import creds
from groq import Groq
from gtts import gTTS
from playsound import playsound
os.environ["GROQ_API_KEY"] = creds.api

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


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
                chat_completion = client.chat.completions.create(
                    messages=[
                         {
                            "role": "user",
                             "content": "act like an ai robot named jessi,only give short ans,and resond to like human like replaying in  short ans ans to this question inshort like a conversation this is the question dont mind the exit in the end of the question here question=   "+ text,
                        }
                    ],
                    model="llama3-70b-8192",
                )
                tts = gTTS(text=chat_completion.choices[0].message.content, lang='en')
                filename = "convertedtext.mp3"
                tts.save(filename)
                print("Audio file generated successfully")

                # Play the audio file
                playsound(filename)
                print("Audio file played successfully")
                print(chat_completion.choices[0].message.content)
                print("Stopping the program")
                break

    except:
        print("u should say something ")
        r = sr.Recognizer()
        continue
    