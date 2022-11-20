import time
import keyboard
import pyautogui
import mouse
import threading

keyboard.wait("space")
former_x, former_y = mouse.get_position()


class MyThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        find()


class MySecondThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        auto_click()


def auto_click():
    while True:
        x, y = mouse.get_position()
        if former_x - 128 < x < former_x + 128 and former_y - 128 < y < former_y + 128:
            mouse.click()
        time.sleep(0.01)


def find():
    try:
        img = pyautogui.screenshot()
        x, y, a, b = pyautogui.locate("cookie2.png", img, confidence=0.6, grayscale=True)
        if x == "NoneType" or y == "NoneType":
            return
        pyautogui.click(x+48, y+48)
        pyautogui.moveTo(former_x, former_y)
    except:
        pass


MySecondThread().start()
MySecondThread().start()
while True:
    MyThread().start()
    time.sleep(0.1)
