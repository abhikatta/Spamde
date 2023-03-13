import string
import pyautogui
import random
import time
import sys
sys.path.append('./')


def spam_random_string(spam_count):
    print("you have 3 seconds")
    time.sleep(3)
    while (spam_count > -1):
        size = random.randint(1, 20)
        msg = (''.join(random.choices(string.ascii_letters, k=size))).lower()
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        spam_count -= 1


def take_input_from_cli():
    spam_count = int(input("enter spam count:"))
    spam_random_string(spam_count)


take_input_from_cli()


''' 
TODO:
1. Fix everything 
2. Build GUI
3. Complete the project.
'''
