from gtts import gTTS
tts = gTTS(text = "hey boy how are u This indicates that the myenv virtual environment is currently active. Now,.",lang='en')
tts.save("convertedtexto.mp3")
print("converted successfully")