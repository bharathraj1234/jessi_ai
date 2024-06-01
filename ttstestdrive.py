from gtts import gTTS
from playsound import playsound

# Generate the speech
tts = gTTS(text=" This indicates that the myenv virtual environment is currently active. Now, any Python packages you install using pip will be installed in the myenv virtual environment, and they won’t affect your other Python projects. When you’re done, you can type deactivate to stop using the virtual environment.", lang='en')
filename = "convertedtext.mp3"
tts.save(filename)

print("Audio file generated successfully")

# Play the audio file
playsound(filename)
print("Audio file played successfully")
