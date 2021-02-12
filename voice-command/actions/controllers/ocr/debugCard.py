import numpy as np
import cv2
from mss import mss
from PIL import Image

sct = mss()

def calculatePosition(xStart, yStart, xEnd, yEnd):
    return {
        'top': yStart,
        'left':xStart ,
        'width': xEnd - xStart,
        'height': yEnd - yStart
    }


def screen2Img(screenshot):
    img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
    img = np.array(img)
    return img

def getImg(position):
    screenshot = sct.grab(position)
    img = screen2Img(screenshot)
    return img

def getCircle(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=15, maxRadius=23)

    return circles, gray

cardOnHandPosition = calculatePosition(452, 978, 1472, 1080)

while 1:
    img = getImg(cardOnHandPosition)
    circles, gray = getCircle(img)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        print("---")
        for (x, y, r) in circles:
            cv2.circle(gray, (x, y), r, (0, 255, 0), 4)
            print(x, y, r)

    cv2.imshow('gray scale', np.array(gray))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break