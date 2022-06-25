import pyttsx3     # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime   # pip install datetime
import webbrowser  # pip install webbrowser
import os         # pip install os
import ctypes     # pip install ctypes
import pyjokes   # pip install pyjokes
import subprocess  # pip install subprocess
import requests   # pip install requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Lea 1 point 0 . I am your Assistant Sir Mam.")
    speak("What should i call you sir Mam")
    uname = takeCommand()
    speak("Welcome Mister Mam.Please tell me how may I help you")
    speak(uname)


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "open wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif 'open youtube' in query:
            speak("Opening Youtube.com\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google.com\n")
            webbrowser.open("google.com")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif "good quote" in query:
            try:
                ## making the get request
                response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
                if response.status_code == 200:
                    ## extracting the core data
                    json_data = response.json()
                    data = json_data['data']
                    ## getting the quote from the data
                    speak(data[0]['quoteText'])
                else:
                    speak("Error while getting quote")
            except:
                speak(" Sorry dear sir , mam.Something went wrong! Try Again!")

        elif 'open stack overflow' in query:
            speak("Opening Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'lock my pc' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown /s /t 1")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            musicdir = r"C:\Users\dell\Desktop\Songsplaylist"
            songs = os.listdir(musicdir)
            print(songs)
            random = os.startfile(os.path.join(musicdir, songs[1]))


        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir Mam, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\dell\Desktop\Speech recognition.docx"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by  Ms.Hima, jasjot and Ms.karneet.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely you are a human.")

        elif "why you came to world" in query:
            speak("Thanks to Hima. Further It's a secret")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir Mam")

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Jasjot, Hima and karneet")

        elif 'reason for you' in query:
            speak("I was created as a Minor project. Thank you for asking. ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif "lea" in query:

            wishMe()
            speak("Lea 1 point o in your service Mister")


        elif 'powerpoint presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\Users\dell\Downloads\Speech Recognition System.pptx"
            os.startfile(power)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
