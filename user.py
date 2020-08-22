import pyttsx3
import os
s=input("enter your name ")
pyttsx3.speak("hello," +s )
pyttsx3.speak(s+ "print your choie ")
print("1.for search browser!")
print("2.for search notepad!")
print("3.for search media player!")

p=input("1,2,3")
k=input("enter your choice:like as you want to open in ur system:")


while True:

    if int(p) == 1:
        pyttsx3.speak("which browser do you want!")
        b=input("name of ur browser  ")
        if("browser" in k):
            if("firefox"in b or "mozilla" in b):
                pyttsx3.speak("oh.. u are searching for firefox browser")
                os.system("mozilla firefox")
            elif("microsoft"in b or "explorer"in b):
                pyttsx3.speak("oh.. u are searching for internet explorer")
                os.system("microsoft edge")
            elif("chrome"in b):
                pyttsx3.speak("oh.. u are searching for chrome")
                os.system("chrome")
            else:
                print("your browser is not available")

    elif int(p)==2:
        if("notepad" in k):
            pyttsx3.speak("which notepad do you want!")
            n=input("name of ur editor  ")
            if ("atom" in n or "editor"in n):
                pyttsx3.speak("oh.. u are searching for atom editor")
                os.system("atom")
            elif("notepad"in n):
                pyttsx3.speak("oh.. u are searching for notepad editor")
                os.system("notepad")
            else:
                pyttsx3.speak("your notepad is not available!")

    elif int(p)==3:
        if("media"in k):
            pyttsx3.speak("which media player do you want!")
            m=input("name of ur media player  ")
            if("windows"in m or "wmplayer"in m):
                pyttsx3.speak("oh.. u are searching for windows media player")
                os.system("wmplayer")
            else :
                pyttsx3.speak("sorry your media player is not available!")

    
    elif("quit"in k or "exit" in k):
         break

    else:
        print("your choice is not available!")