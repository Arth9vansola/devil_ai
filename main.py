import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "cce28c019165410c9d884ea23e0c8b05"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")   
    elif "open twitter" in c.lower():
        webbrowser.open("https://x.com/ArthM3333")    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/arth-m-ab6629256/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]    
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")  
        if r.status_code == 200:
            data = r.json() # parse the json response
            articles = data.get('articles',[]) # extract the articles
            for article in articles:
                speak(article['title']) # print the headlines
                    

if __name__ == "__main__":
    speak("Initializing devil...")

while True:
    # listen for the wake word "devin"
    # obtain audio from the microphone
    r = sr.Recognizer()
    

    # print("recognizing")    

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout = 2,phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower() == "devil"):
            speak("Yes sir !!!")
            # Listen for command
            with sr.Microphone() as source:
                print("devil Active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)
        
    
    except Exception as e:
        print("Error; {0}".format(e))        
