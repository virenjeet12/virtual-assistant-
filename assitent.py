import webbrowser
import pyttsx3
import wikipedia
import speech_recognition as sr
import time


# for initital start the assitent program
def hello():
    #  speak("hello viren , i am your desktop assistent..\n Tell me how may i help you..")
       speak("hello viren")

# for convert text to speech 
def speak(text):
     engine = pyttsx3.init()
     voices = engine.getProperty("voices")
     engine.setProperty("voice",voices[1])
     engine.say(text)
     engine.runAndWait()

# for take command from the user and start processing it
def take_command():
    r =sr.Recognizer()

    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source,duration=1)
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        

        try:
            print("Recognizing")

            query = r.recognize_google(audio,language="en-in")
            print("The command is printed : ",query)
        
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")

        except Exception as e:
            print(e)
            print("say that again sir")
            return "None"

    return query

def take_query():
    hello()
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    while(True):
        query = take_command().lower()

        if "open icloud" in query:
            speak("opening gu icloud")
            webbrowser.get('chrome').open_new_tab("https://gu.icloudems.com/corecampus/index.php")
            continue

        elif "open wpl" in query:
            speak("opening women's premier league")
            webbrowser.get('chrome').open_new_tab("https://www.google.com/search?gs_ssp=eJzj4tVP1zc0LE5JiU82sIg3YPRiLi_IAQA9RgXU&q=wpl&oq=&gs_lcrp=EgZjaHJvbWUqCQgCEC4YJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCEC4YJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQk2NTM4MWowajeoAgiwAgE&sourceid=chrome&ie=UTF-8")
            continue

        elif "bye" in query:
            speak("bye viren")
            exit()

        elif "from wikipedia" in query:
            speak("checking the wikipedia")
            query = query.replace("wikipedia","")

            result = wikipedia.summary(query,sentences=4)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif "tell me your name" in query:
            print("i am deepak your desktop assistant")
            speak("i am deepak your desktop assistant")

# take_query()
            
        # for advanced use

def initial_start():

    r =sr.Recognizer()

    with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source,duration=1)
            print("listening")
            r.pause_threshold = 1
            audio = r.listen(source)

    try:
            print("Recognizing")

            query = r.recognize_google(audio,language="en-in")
            print("The command is printed : ",query)
        
    except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
            initial_start()

    except Exception as e:
            print(e)
            print("say that again sir")
            initial_start()
            return "None"
    return query



# starttime = time.time()
while True:                                                        
    # query_a = initial_start()
    query_a = input("enter hello : ")
    if "hello" in query_a:
        take_query()
    # Remove the Time taken by code to execute
    # time.sleep(60.0 - ((time.time() - starttime) % 60.0))



               
          