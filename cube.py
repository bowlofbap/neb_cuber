import cv2
import time
import pyautogui
import win32gui
import numpy as np
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

def grab_screenshot():
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
    left = 430
    top = 255
    right = 945
    bottom = 570
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = img.crop((left, top, right, bottom))
    return cv2.cvtColor(np.array(im1), cv2.COLOR_RGB2BGR)

def detect_page1(img):
    text = pytesseract.image_to_string(img)
    if "Use an Alien Cube" in text:
        return True
    return False
 
def main():
    img = grab_screenshot()
    detected_page_1 = detect_page1(img)
    if detected_page_1:
        print("On page1")
    else:
        print("Not page1")

if __name__ == "__main__":
    main()