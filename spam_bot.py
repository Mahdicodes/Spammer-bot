from pynput.keyboard import Key,Controller
import time

keyboard  = Controller()
# the spam will start after this time 
# This is the chance number when you have the opportunity to choose where you want to spam
time.sleep(5)
# your message text
message = 'your message'
count = 0

for num in range(count)
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # time between every message
    time.sleep(0.1)
