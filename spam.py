import argparse
import string
import pyautogui
import random
import time
import sys


parser = argparse.ArgumentParser(
    description='Spam some text a given number of times',
    add_help=True,
    epilog="Want to add something?, visit https://github.com/Abhinay-Katta/Spam-with-Python",
    prog="spam",
    usage="%(prog)s [-h|--help] [-v|--version] <number> <string>"
)
parser.add_argument('text', type=str, help='The text to spam')
parser.add_argument('n', type=int, help='The number of times to spam the text')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.6')
parser.add_help

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
