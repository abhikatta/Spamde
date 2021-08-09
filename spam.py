import pyautogui, time
time.sleep(2)
f = open ("D:\VS Code\script",'r')
d = open ("script",'r')
for word in d:
    pyautogui.typewrite(word)
    pyautogui.press("enter")  

Method-2 :
+++++++++++++
msg = input("Enter your message:")
n = input("How many times?: ")
time.sleep(2)
for i in range(0,int(n)):
    pyautogui.typewrite(msg + '\n')
     