import pyautogui
import time
import sys
sys.path.append('./')


def spam_from_msg():
    time.sleep(2)
    # add the path to the script file here. script file is a txt file
    f = open("path", 'r')
    d = open("script", 'r')
    for word in d:
        pyautogui.typewrite(word)

        pyautogui.press("enter")
