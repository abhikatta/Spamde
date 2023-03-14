import argparse
import string
import pyautogui
import random
import time
import sys


parser = argparse.ArgumentParser(
    description='Pass 2 args one as a string(text) and other a number(n) to spam the text n number of times, if unknown type of arg is passed a random string(message) will be spammed random number of times.')
parser.add_argument(
    'arg1', help=' should be a string or number')
parser.add_argument(
    'arg2', help='if arg1 is a nummer this should be a string or vice versa')
args = parser.parse_args()
argss = sys.argv

spam_count = random.randint(10, 100)
for arg in argss[1:]:
    if arg.isdigit() == True:
        spam_count = int(arg)
    elif arg.isalpha() == True:
        msg = arg
    else:
        msg = ''.join(random.choices(string.ascii_letters,
                                     k=random.randint(1, 20))).lower()

print("You have 3 seconds")
time.sleep(3)
while (spam_count > 0):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    spam_count -= 1
