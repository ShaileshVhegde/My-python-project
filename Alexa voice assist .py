#pip install speechrecognition
#pip install setuptool
#pip install pyaudio
#pip install pyttsx3
# pip install pocketsphinx
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibreray

recognisor=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if"open youtube"in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif"open facebook"in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif"open song"in c.lower():
        webbrowser.open("https://youtu.be/vrjndQ4BXMU?si=iVqkx9d6mPC26GWS")
    elif"open google"in c.lower():
        webbrowser.open("https://www.google.com")
    elif"open instagram"in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibreray.music(song)
        webbrowser.open(link)
        
        
    else:
          output = aiProcess(c)
          speak(output) 

        
        
    pass
if __name__=="__main__":
     speak("welcome to hello voice assistetent")
while True:
    r=sr.Recognizer()
    print("im listining....")
    try:
        with sr.Microphone() as source:
            print("recognising")
            audio=r.listen(source,timeout=2,phrase_time_limit=3 )
        word=r.recognize_google(audio)
        
        if(word.lower()=="alexa"):
            speak("yes how can i help you")
            with sr.Microphone() as source:
                print("assistent active")
                audio=r.listen(source)
                command=r.recognize_google(audio)            
                processcommand(command)
                
                
    except Exception as e:
        print("sorry {0}".format(e))
   
      
    
       

    
