# project_on_ai
from math import e
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtpd
import speech_recognition as sr
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int (datetime.datetime.now().hour)
    if hour >=0 and hour<12 :
        speak("Good morning SIR")
    elif hour>=12 and hour <18 :
        speak(" Good Afternoon Sir")
    elif hour>=18 and hour <=21 :
        speak (" Good evening Sir")
    else:
        speak (" Good night Sir")
    # speak("hi . mera  naam  ALEX  hai . or mai aapka ai assistant hu, mai aapki kaiise help kar saktaa hu ")  
    speak("Hi I am mini . I am your A I voice assistant . How can I help you Sir ")  
def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak ... ")
        r.pause_threshold = 0.7
        r.energy_threshold=700
        r.phrase_threshold= 0.7 
        audio = r.listen(source)
    try:
        print (" Recognizing ....")
        query = r.recognize_google(audio,language='hindi')
        print(f"You said : {query}\n ") 
    except Exception as e:
        print (e)
        print("Say that again please ...")
        return"None"
    return query    
# def sendEmail(to,content):
#     server= smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('vinoddevil824@gmail.com','password')
#     server.sendmail('vinoddevil824@gmail.com',to,content)
#     server.close()
if __name__== "__main__":
    # speak("Hello Vinod")
    wishme()
    while True:
       query = takecommand().lower()
       if 'wikipedia' in query:
            speak(" Searching  Wikipedia  ...")
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
       elif 'open youtube'in query:
            webbrowser.open("www.youtube.com")
       elif 'open chrome ' in query:
            webbrowser.open(webbrowser)
       elif 'play music' in query:
           webbrowser.open("www.jiosaavn.com")
       elif 'meet'in query:
           webbrowser.open("https://meet.google.com/")
       elif 'google' in query:
            webbrowser.open("www.google.com")
    #    elif 'movie' :
    #        movie_dir ='F:\\rockpaper'
    #        movies = os.listdir(movie_dir) 
    #        os.startfile(os.path.join(movie_dir,movies[1]))
       elif "time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"Sir, THE Time is {strTime}")
       elif 'open code' in query:
           vscode="C:\\Users\\me\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(vscode)
       elif 'photoshop' in query:
           photoshop="C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
           os.startfile(photoshop)
       elif 'open chrome' in query:
           chrome="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
           os.startfile(chrome)
    #    elif 'email to vinod' in query:
    #        try:
    #            speak("What should I write")
    #            content= takecommand()
    #            to = "vinoddevil824@gmail.com"
    #            sendEmail(to,content)
    #            speak("Email has been sent!")
    #        except Exception as e:
    #            print(e)
    #            speak (" i am not able to send email.")
  

   

        
         




        


