import numpy as np
import cv2
from mss import mss
from PIL import Image

def calculatePosition(xStart, yStart, xEnd, yEnd):
    return {
        'top': yStart,
        'left':xStart ,
        'width': xEnd - xStart,
        'height': yEnd - yStart
    }

cardOnHandPosition = calculatePosition(452, 978, 1472, 1044)
enemyMonster = calculatePosition(469, 82, 1404, 263)
ownMonster = calculatePosition(489, 806, 1428, 973)
enemyField = calculatePosition(360, 275, 1524, 542)
ownField = calculatePosition(373, 551, 1533, 799)

mon = cardOnHandPosition

sct = mss()

while 1:
    screenshot = sct.grab(mon)
    img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
    img = np.array(img)
    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.5, 41, minRadius=1, maxRadius=100)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(gray, (x, y), r, (0, 255, 0), 4)
            # cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    cv2.imshow('test', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break