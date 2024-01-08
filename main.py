import datetime

import pyttsx3

import speech_recognition_google as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
index = 1
engine.setProperty('voice', voices[1].id)

# list voices
# for voice in voices:
#    print(f'index-> {index} -- {voice.name}')
#    index += 1
# engine.runAndWait()

# voice selector?

author = "Jo"

# define the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# define the greetings function
def greetings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good Morning {author}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon {author}")
    else:
        speak(f"Good Evening {author}")
    speak(f"what would you like me to do for you today?")

# define the take command function - need API setup to work 
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("listening...")
      r.pause_threshold = 1  # seconds before the input is taken after last spoken word
      audio = r.listen(source)
    try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='en-us')
      print(f"user said: {query}\n")
    except Exception as e:
        print(f"Sorry {author}, I did not get that, could you repeat please?...")
        return "None"
    return query

if __name__ == "__main__":
    speak(f"welcome{author}, I am nina")
    greetings()
    engine.runAndWait()
