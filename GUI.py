
import pyautogui
import time


def spam_from_text():
    return print('ASDSADAS')

    d = open("script", 'r')
    # add the path to the script file here. script file is a txt file
    '''TODO:
        1. add a browse button to spam from a text file,(any file)
        
    '''
    time.sleep()
    for word in d:
        pyautogui.typewrite(word)
    pyautogui.press("enter")
    return 0


def spam_from_input():
    return print("ASD")
    try:
        msg_prompt = 'Enter the message you want to spam:'
        msg = str(input())
        wait_time_prompt = 'Enter the time you want to wait before spam starts:'
        wait_time = int(input())
        spam_count_prompt = 'Enter the number of times you want to spam your message:'
        spam_count = int(input())
    except Exception as e:
        print(e)

    # add the path to the script file here. script file is a txt file
    while (wait_time >= 0):
        warn_time_prompt = f'Open the textarea you want to spam at in {i} seconds!'
        wait_time -= 1
        time.sleep(1)

        # TODO print warn time

    time.sleep()
    for word in msg*spam_count:
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
    return 0
    print('spamworked')
