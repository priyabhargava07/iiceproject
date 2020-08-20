import os 
import pyttsx3 as py
py.speak("welcome to my application")
print()
print(" 1: to open chrome browser")
print(" 2: to open vlc media player")
print(" 3: to open firefox")
print(" 4: to open notepad ")
print(" 5: to open telegram") 
print(" 6: to open whatsapp")
print(" 7: to exit ")
print()
py.speak("please enter want to open")
while(1):
	
	print("enter your choice: " , end=" ")
	p=input()
	if   (("run" in p) or ("execute" in p)  or ("open" in p)) and (("chromre" in p) or ("browser" in p)):
		py.speak("opening chrome browser")
		os.system("chrome.exe")

	elif (("run" in p) or("execute" in p) or("open" in p)) and (("player" in p)or("vlc" in p)):
		py.speak("opening vlc media player")
		os.system("vlc.exe")
	
	elif (("run" in p)or ("execute" in p) or("open" in p)) and (("firefox" in p) or ("firefox browser" in p)):
		py.speak("opening firefox browser")
		os.system("firefox.exe")

	elif (("run" in p) or("execute" in p) or("open" in p)) and (("notepad" in p) or("editor" in p)):
		py.speak("opening notepad")
		os.system("Notepad")
	
	elif (("run" in p) or("execute" in p) or ("open" in p)) and ("telegram" in p):
		py.speak("opening telegram application")
		os.system("Telegram.exe")
	
	elif (("run" in p) or("execute" in p) or("open" in p)) and ("whatsapp" in p) :
		py.speak("opening whatsapp application")
		os.system("WhatsApp.exe")

	elif  ("exit" in p) or ("terminate" in p) or ("quit" in p):
		py.speak("iam turing off the  program")
		break

	else:
		py.speak("you have chose something wrong please try again")
		print("you have choose wrong option ! try again")