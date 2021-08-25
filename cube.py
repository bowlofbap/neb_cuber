import cv2
import time
import pyautogui
import win32gui
import numpy as np
import pytesseract
from PIL import ImageGrab
from directkeys import PressKey, ReleaseKey, ClickKey, DIRECTIONS

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path = "./ss/img.png"

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

def sss():
    win32gui.EnumWindows(enum_cb, toplist)

    aurora = [(hwnd, title) for hwnd, title in winlist if 'aurora' in title.lower()]
    aurora = aurora[0]
    hwnd = aurora[0]

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)

    #crop image top left
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = img.size
    
    # Setting the points for cropped image
    left = 0
    top = 0
    right = 0
    bottom = 0
    
    # Cropped image of above dimension
    # (It will not change original image)
    #im1 = img.crop((left, top, right, bottom))
    img.save(path)

def grab_screenshot(l, t, r, b):
    win32gui.EnumWindows(enum_cb, toplist)

    aurora = [(hwnd, title) for hwnd, title in winlist if 'aurora' in title.lower()]
    aurora = aurora[0]
    hwnd = aurora[0]

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)

    #crop image top left
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = img.size
    
    # Setting the points for cropped image
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = img.crop((l, t, r, b))
    return cv2.cvtColor(np.array(im1), cv2.COLOR_RGB2BGR)

def move_and_click():
    aurora = [(hwnd, title) for hwnd, title in winlist if 'aurora' in title.lower()]
    aurora = aurora[0]
    hwnd = aurora[0]
    rect = win32gui.GetWindowRect(hwnd)
    pyautogui.click(rect[0] + 430 + 50, rect[1] + 255 + 50)

def detect_string_in_page(img, string):
    text = pytesseract.image_to_string(img)
    if string in text:
        return True, text
    return False, text
 
#poc
'''
def main():
    print(text1)
    if detected_page_1:
        print("On page1")
        ClickKey(DIRECTIONS["DOWN"])
        ClickKey(DIRECTIONS["DOWN"])
        ClickKey(DIRECTIONS["DOWN"])
        ClickKey(DIRECTIONS["DOWN"])
        ClickKey(DIRECTIONS["DOWN"])
        ClickKey(DIRECTIONS["SPACE"])
        time.sleep(1)
        img2 = grab_screenshot(640, 325, 945, 570)
        detected_page_2, text2 = detect_string_in_page(cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY), "] Nebulite")
        print(text2)
        if detected_page_2:
            move_and_click()
            print("On page2")
        else:
            print("Not Page 2")
    else:
        print("Not page1")
'''
def main():
    detected = False
    while not detected:
        ClickKey(DIRECTIONS["SPACE"])
        time.sleep(.2)
        img = grab_screenshot(643, 383, 913, 445)
        correct_page, return_text = detect_string_in_page(img, "Nebulite (")
        if not correct_page:
            print("Go to the Socket Master and select the neb you want to cube.")
            return
        detected, text1 = detect_string_in_page(img, "All Stats: +6%")
        print(text1)
        time.sleep(.1)

if __name__ == "__main__":
    main()