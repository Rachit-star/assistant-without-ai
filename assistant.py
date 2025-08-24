import pyttsx3
import speech_recognition as sr
import webbrowser


r = sr.Recognizer()




def say(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    
def executing(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

            

if __name__ == "__main__":
    say("Hello! I am Meo.")
    
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = r.listen(source, timeout=3, phrase_time_limit=5)
               
            except sr.WaitTimeoutError:
                continue  

        print("Recognizing...")
        try:
            text = r.recognize_google(audio)
            text_lower = text.lower()

            if "exit" in text_lower or "quit" in text_lower:
                say("Goodbye!")
                break   # stop loop here

            elif "mio" in text_lower:
                say("Yes, I am Meo speaking")
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    executing(command)
                    
                

            else:
                print("You said:", text)
                say(f"You said: {text}")    

        except sr.UnknownValueError:
            print("Could not understand audio")
            say("I could not understand what you said")
        except sr.RequestError as e:
            print("Recognition error:", e)
            say("There was an error with the recognition service")
