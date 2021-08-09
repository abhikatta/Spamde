import pyautogui, time
time.sleep(2)
f = open ("path",'r') #add the path to the script file here. script file is a txt file  
d = open ("script",'r')
for word in d:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
