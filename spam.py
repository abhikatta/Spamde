import string
import pyautogui
import random
import time
import sys
sys.path.append('./')


def spam(msg, spam_count):
    print("you have 3 seconds")
    time.sleep(3)
    while (spam_count > 0):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        spam_count -= 1


def take_input():
    instr = "0 for msg and spam_count\n1 for random strings and spam_count\n2 for file and spam_count\n3 to quit"
    print("Instructions:\n")
    print(instr)
    print("\n")
    inputs = input("Enter 0 or 1 or 2 or 3:\n")
    if (inputs == "0"):
        msg = input("\nEnter msg you want to spam:\n")
        spam_count = int(input("\nEnter how many times you want to spam:\n"))
        spam(msg, spam_count)
    elif (inputs == "1"):
        spam_count = int(input("\nEnter how many times you want to spam:\n"))
        print("you have 3 seconds")
        time.sleep(3)
        while (spam_count > 0):
            size = random.randint(1, 20)
            msg = (''.join(random.choices(string.ascii_letters, k=size))).lower()
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
            spam_count -= 1

    elif (inputs == "2"):
        spam_file = input("\nThrow in the address of the file:\n")
        spam_count = int(input("\nEnter how many times you want to spam:\n"))
        open_spam_file = open(spam_file, 'r')
        for i in open_spam_file:
            pyautogui.typewrite(i)
            pyautogui.press("enter")
    elif (inputs == "3"):
        quit
    else:
        print("Here are the instructions again,read them carefully:")
        take_input()


take_input()
