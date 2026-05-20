from gtts import gTTS
import playSound
text=input("Enter the text you want to convert to speech: ")
sound=gTTS(text=text,lang='en',slow=False)
sound.save("converted.mp3")
playSound.playsound("converted.mp3")