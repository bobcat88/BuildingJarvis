import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
index = 1
engine.setProperty('voice', voices[1].id)

# list voices
# for voice in voices:
#    print(f'index-> {index} -- {voice.name}')
#    index += 1
# engine.runAndWait()

# voice selector ?

author = "Jo"

# define the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    speak(f"welcome{author}, I am nina")
    speak(f'what would you like me to do for you today?')
    engine.runAndWait()
