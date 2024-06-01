import os
import creds
from groq import Groq
from gtts import gTTS
from playsound import playsound


os.environ["GROQ_API_KEY"] = creds.api

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
while True:
    prompt = input("enter ur question here  ")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "u are jessi a human like robot u are here to help human ans the given question in short and human like response and dont say like here is my respone any like a bot replay act like a human like way so here is the question to u make sure you ans very very short ans"+prompt,
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
