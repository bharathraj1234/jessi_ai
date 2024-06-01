import os
import creds
from groq import Groq
from gtts import gTTS
from playsound import playsound


os.environ["GROQ_API_KEY"] = creds.api

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "write very short ans on explain about urself ans like u are a human robot named jessi and ans like short like human do ",
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
