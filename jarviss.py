import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTimer, QDate, Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import jarvis

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# speak functions


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# wishme functions


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am Friday. Please tell me how may i help you")
    print("I am Friday. Please tell me how may i help you")

# take command funcation audio input and print result


def takeCommand():

    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr. Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        # using google for voice recognition.
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User queryywill be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

# class MainThread(QThread):
#     def __init__(self):
#         super(MainThread,self).__init__()
#     def run(self):
#         self.TaskExecution 

#startExecution = MainThread()
if __name__ == "__main__":
    WishMe()
    # takeCommand()
    while True:
        query= takeCommand().lower()  # converting user query into lower case

        # Login for executing tasks based on query
        #funny commands
        

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'how are you friday' in query:
            speak("I am fine sir and you")


        elif 'who is sweta' in query:
            speak("sweta is the sister in law of ours and gulshan bhai")

        elif 'hello friday' in query:
            speak("I am always ready for you sir")

        elif 'will you marry me' in query:
            speak("itne khubsurat vicharo ke liye ke shukriya main hamesha ke liye aapki sahahika hu")
            
        elif 'open youtube' in query:
            webbrowser.open_new_tab("youtube.com")


        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")
# play music function
        elif 'play music' in query:
            speak("ok sir just wait a one seconds ")
            s = random.randint(0,3)
            print(s)
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[s]))
        elif 'play song' in query:
            speak("ok sir just wait a one seconds ")
            s = random.randint(0,3)
            print(s)
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[s]))
        elif 'ganna' in query:
            speak("ok sir just wait a one seconds ")
            s = random.randint(0,3)
            print(s)
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[s]))
           
# play next music function
        elif 'next song' in query:
            s = random.randint(0,3)
            print(s)
            speak("Ok sir")
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[s]))
                   
# the time functions          
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
# open office functions
        elif 'open powerpoint' in query:
            PowerPointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(PowerPointPath)

        elif 'powerpoint' in query:
            PowerPointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(PowerPointPath)
        
        elif 'open word' in query:
            MsWord = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(MsWord)
            continue
        elif 'ms word' in query:
            MsWord = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(MsWord)

   # open chrome browser         
        elif 'google chrome' in query:
            GoogleChrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(GoogleChrome)
        elif 'chrome' in query:
            GoogleChrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(GoogleChrome)
        elif 'chrome browser' in query:
            GoogleChrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(GoogleChrome)

        elif "search on chrome" in query:
            speak("What should in search sir")
            search = takeCommand()
            chrompath ="C://Program Files//Google//Chrome//Application//chrome.exe %s"
            webbrowser.get(chrompath).open_new_tab(search+'.com')
        elif "search on google" in query:
            speak("What should in search sir")
            search = takeCommand()
            chrompath ="C://Program Files//Google//Chrome//Application//chrome.exe %s"
            webbrowser.get(chrompath).open_new_tab(search+'.com')
# shoutdown functions
        elif "shutdown" in query:
            speak("do you really want to shoutdown")
            reply = takeCommand()
            if "yes" in reply:
                speak(f"Ok sir i am going to")
                os.system('shutdown /s /t 1')
            else:
                speak("I dont understand please tell me again")
                
        elif "restart" in query:
            speak("do you really want to restart")
            reply = takeCommand()
            if "yes" in reply:
                speak("Thank you sir")
                os.system('shutdown /r /t 0')
            else:
                speak("I dont understand please tell me again")

        elif "log out" in query:
            speak("do you really want to logout")
            reply = takeCommand()
            if "yes" in reply:
                os.system('logout -1')
            else:
                break
        
 
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/download.jpg")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
friday = Main()
friday.show()
exit(app.exec_())