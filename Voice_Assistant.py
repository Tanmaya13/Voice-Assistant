import pyttsx3                                                                      
import datetime                                                 # to know the current date and time                 
import speech_recognition as sr                                                     
import wikipedia                                                # for searching in wiki                             
import smtplib                                                  # for email sending                                 
import webbrowser as wb                                         # to search in chrome
import os                                                       # logout, shutdown, restart
import pyautogui                                                # for taking screenshots                            
import psutil                                                   # for showing cpu and battery                       


engine = pyttsx3.init()



# VOICE OPTIONS AND SPEAK RATE
#------------------------------------------------------------------------------------------------------------------------------------
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)                       # voices[1].id  for female voice 
newVoiceRate = 150                                              # 150 wpm
engine.setProperty('rate', newVoiceRate)    
#------------------------------------------------------------------------------------------------------------------------------------



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



#------------------------------------------------------------------------------------------------------------------------------------
# TIME FUNCTION

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")     
    speak(Time)


# DATE FUNCTION

def date():
    year = int(datetime.datetime.now().year)    
    month = int(datetime.datetime.now().month)  
    day = int(datetime.datetime.now().day)      
    speak("today's date is")
    speak(day)
    speak(month)
    speak(year)
#---------------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------------
# GREETING FUNCTION

def wishme():
    speak("I am Hailee. I am your AI voice Assistant.")
    speak("Welcome back sir!")
    
    hour = datetime.datetime.now().hour
    if(hour >= 6 and hour <= 12):
        speak("Good morning!")
    elif(hour > 12 and hour < 18):
        speak("Good afternoon")
    else:
        speak("Good evening!")

#--------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------
# TAKE COMMAND FUNTION

def takecommand():
    speak("what can I do for you Sir?")
    r = sr.Recognizer()
    with sr.Microphone() as source:                                 # our system microphone as the source to take voice command
        print("Listening...")
        r.pause_threshold = 1                                       
        audio = r.listen(source)                                    # microphone will listen to our voice and store in 'audio' variable
    try:
        print("Recognizing...")         
        query = r.recognize_google(audio, language = 'en = in')    
        print(query)                                                # query will be printed in the console
    except Exception as e:              
        print(e)
        speak("Say that again please...")
        return "None"
    return query
#--------------------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------------------
# EMAIL SENDING FUNCTION

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)                    # 587 is the port number
    server.ehlo()                                                   # checking the connection with the stmp server of gmail
    server.starttls()     
    server.login("sender@gmail.com","sendergmailpassword")      
    server.sendmail("sender@gmail.com", to, content)        
    server.close()
#------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------
# TAKING SCREENSHOT FUNCTION

def screenshot():
    img = pyautogui.screenshot()                                      
    img.save(r"C:\Users\TANMAYA\projects\Voice Assistance\ss.png")    # saving the picture
#------------------------------------------------------------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------------------------------------------------
# CPU AND BATTERY DISPLAY FUNCTION

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu usage is" + usage + "percent")

    battery = psutil.sensors_battery()            
    speak("battery is at")
    speak(battery.percent)
    speak("percent")
#-------------------------------------------------------------------------------------------------------------------------------------------




# MAIN FUNCTION
# all the above functions are called from here

if __name__=="__main__":
    
    wishme()

    while True:
        query = takecommand().lower()  
        print(query)

        if "time" in query:     
            time()              


        elif "date" in query:   
            date()


        elif "how are you" in query:
            speak("I am good sir")


        # STOPPING WHILE LOOP
        elif "offline" in query:    
            speak("Ok sir! Have a good day!")                  
            break                                                   # while loop breaks


        # SEARCHING IN WIKIPEDIA
        elif "wikipedia" in query:                                  
            speak("Searching sir...")
            query = query.replace("wikipedia", "") 
            result = wikipedia.summary(query, sentences = 2)    
            speak(result)                                           


        # SENDING EMAIL
        elif "send email" in query:                                 
            try:
                speak("what is the message you want to Mail sir?")
                content = takecommand()
                to = "receiver@gmail.com"       
                sendemail(to, content)
                speak("sir! Your email has been sent successfully!")
            except Exception as e:
                speak(e)
                speak("unable to send the email sir")

        
        # SEARCHING IN CHROME
        elif "search in chrome" in query:                           
            speak("what do you want to search sir?")
            # path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takecommand().lower()
            wb.open_new("http://www." + search + ".com")     
            speak("here is your result sir")                 
                                                            

        # SHUTDOWN LOGOUT RESTART
        elif "logout" in query:
            os.system("shutdown - l")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")


        # PLAYING SONG
        elif "play song" in query:
            songs_dir = "F:\musics\music"                   
            songs = os.listdir(songs_dir)                   
            os.startfile(os.path.join(songs_dir, songs[0]))


        # REMEBER FUNCTION
        elif "remember" in query:
            speak("what should I remember?")
            data = takecommand()
            speak("done sir")
            remember = open("data.txt", "w") 
            remember.write(data)                        
            remember.close()

        elif "remind me" in query:
            remember = open("data.txt", "r")    
            speak(remember.read())              
            speak("that's all, you told me to remember sir")


        # SCREENSHOT FUNCTION
        elif "screenshot" in query:
            screenshot()
            speak("screenshot taken sir")


        # CPU AND BATTERY FUNCTION
        elif "cpu" in query:
            cpu()


            


