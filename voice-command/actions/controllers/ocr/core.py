import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import tensorflow as tf
import scipy
from skimage.color import rgb2gray
from skimage.transform import resize
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

model = tf.keras.models.load_model(os.path.abspath(os.getcwd()) + "\\actions\\controllers\\ocr\\models\\newmodel.h5")
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

def countCard(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=15, maxRadius=20)

    if circles is None:
        return 0

    return len(circles[0])

def getNumberOfCards(position):
    img = getImg(position)
    return countCard(img)

def getNumberCharacter(img):
    grayscale = rgb2gray(img)
    resized_image = resize(grayscale, (128, 256), order=0, preserve_range=True, anti_aliasing=False)
    resized_image = resized_image.reshape((1, 128, 256, 1))
    pred = model.predict(resized_image)
    return np.round(pred, 0)[0][0]

def countCharacter(position):
    img = getImg(position)
    return getNumberCharacter(img)

def getNameImg():
    name = str(int(time.time() * 1000))
    return "./data/" + name + ".jpg"

def captureScreen():
    img = sct.grab(ownField)
    img = Image.frombytes('RGB', (img.width, img.height), img.rgb)
    img.save(getNameImg())

    img = sct.grab(enemyField)
    img = Image.frombytes('RGB', (img.width, img.height), img.rgb)
    img.save(getNameImg())

    img = sct.grab(ownMonster)
    img = Image.frombytes('RGB', (img.width, img.height), img.rgb)
    img.save(getNameImg())

    img = sct.grab(enemyMonster)
    img = Image.frombytes('RGB', (img.width, img.height), img.rgb)
    img.save(getNameImg())

cardOnHandPosition = calculatePosition(452, 978, 1472, 1080)
enemyMonster = calculatePosition(469, 82, 1404, 263)
ownMonster = calculatePosition(489, 806, 1428, 983)
enemyField = calculatePosition(360, 275, 1533, 470)
ownField = calculatePosition(373, 600, 1533, 799)

def getResources():

    cards = getNumberOfCards(cardOnHandPosition)
    countEnemyMonster = countCharacter(enemyMonster)
    myMonster = countCharacter(ownMonster)
    countEnemyField = countCharacter(enemyField)
    myField = countCharacter(ownField)

    return {
        "cards": cards,
        "enemyMonster": countEnemyMonster,
        "myMonster": myMonster,
        "enemyField": countEnemyField,
        "myField": myField
    }

# draw circle code
    # if circles is not None:
    #     circles = np.round(circles[0, :]).astype("int")
    #     for (x, y, r) in circles:
    #         cv2.circle(gray, (x, y), r, (0, 255, 0), 4)