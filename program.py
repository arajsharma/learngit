import os 
p=input('enter your choice : ')
print("type BROWSER for run browser ")
print("type MEDIA PLAYER for run media player ")
print("type EDITOR for run editor ")
print("type GAME for play the game ")
print("type QUIT for quit  ")
while True:
    if("browser" in p):
        n=input("which browser do you want to use : ")
        if("chrome" in n or "google" in n):
            os.system("chrome")
        elif("microsoft" in n or "edge" in n):
            os.system("microsoft edge")
        elif("mozilla" in n or "firefox" in n):
            os.system("mozilla firefox")
        elif("other" in n): 
            print("your choice is not available in this system!")
        else:
            break
            
    elif("media"  in p):
        m=input("which media player do you want to use : ")
        if("wmplayer" in m or "media" in m):
            os.system("wmplayer")
        elif("vlc" in m or "player" in m):
            os.system("vlc media player")
        elif("netflix" in m ):
            print("your choice is not available in this system!")
        else:
            break
            
    elif("editor" in p):
        e=input("which editor do you want to use : ")
        if("notepad" in e or "editor" in e):
            os.system("notepad")
        elif("atom" in e or "text" in e):
            os.system("atom")
        elif("vs" in e or "code" in e):
            os.system("vscode")
        elif("sublime" in e):
            print("your choice is sublime ,notepad++ which is not available!")
        else:
            break
            
            
    elif("game" in p):
        g=input("which game do you want to play : ")
        if("saga" in g or "candy" in g):
            os.system("candy crush saga")
        else:
            print("your game is not available!")
            
    elif("quit" in p or "exit"in p):
        break
    else:
        print("your choice is not available ")
        print("sorry for inconvenience!")
        print("i'm working on your choice !")
        print("thanks for using this!")
            
        
        
    