import pyautogui
from .ocr.core import getResources

def calculatePosition(startPoint, endPoint, itemWidth, xDefault, yDefault, selectIdx, max):
    MAX = endPoint
    MIN = startPoint
    CARDWIDTH = itemWidth
    WIDTH = MAX - MIN
    WIDTHCENTER = (MAX + MIN) / 2

    x = xDefault
    y = yDefault
    if WIDTH / CARDWIDTH > max:
        handWidth = CARDWIDTH * max
        sizeToCenterHand = handWidth / 2
        startPoint = WIDTHCENTER - sizeToCenterHand
        selectPoint = CARDWIDTH * selectIdx - CARDWIDTH / 2
        x = startPoint + selectPoint
    else:
        newCardWidth = WIDTH / max
        x = MIN + newCardWidth * selectIdx - newCardWidth / 2

    return x, y

def getCardPosition(selectIdx, max):
    MAX = 1449
    MIN = 480
    CARDWIDTH = 165

    x = 960
    y = 1040

    return calculatePosition(MIN, MAX, CARDWIDTH, x, y, selectIdx, max)

def getCharacterPosition(selectIdx, max):
    MAX = 1404
    MIN = 513
    CARDWIDTH = 155

    x = 960
    y = 900

    return calculatePosition(MIN, MAX, CARDWIDTH, x, y, selectIdx, max)

def getFieldPosition(selectIdx, max):
    MAX = 1538
    MIN = 379
    CARDWIDTH = 280

    x = 960
    y = 708
    return calculatePosition(MIN, MAX, CARDWIDTH, x, y, selectIdx, max)

def selectCard(number):
    resources = getResources()
    print("select card", number)
    x, y = getCardPosition(number, resources["cards"])
    pyautogui.moveTo(x, y)

def selectEnemyChracter(number, place):
    print("select enemy character", number)
    resources = getResources()
    x, y = getCharacterPosition(number, resources["enemyMonster"])
    pyautogui.click(x=x, y=y - 727) 

def selectFriendlyCharacter(number, place):
    print("select my character", number)
    resources = getResources()
    x, y = getCharacterPosition(number, resources["myMonster"])
    pyautogui.click(x=x, y=y) 

def selectCharacter(number, mode='friendly', place='onStage'):
    if mode == 'friendly':
        selectFriendlyCharacter(number, place)
    elif mode == 'enemy':
        selectEnemyChracter(number, place)

def dragToPosition(x, y):
    pyautogui.dragTo(x, y, 0.3, button='left')
    print("drag2", x, y)

def pullEnemy(number):
    resources = getResources()
    x, y = getFieldPosition(number, resources["myField"])
    dragToPosition(x, y)
    print("pull", number)

def blockEnemy(number):
    resources = getResources()
    x, y = getFieldPosition(number, resources["enemyField"])
    dragToPosition(x, y)
    print("block", number)

def endTurn():
    pyautogui.click(x=1664, y=545) 
    print("pass")

def attackAll():
    selectCharacter(1)
    pyautogui.mouseDown()
    pyautogui.moveTo(1404, 850, 0.5)
    dragToMid()
    pyautogui.mouseUp()
    print("attack all")

def dragToMid():
    midX = 985
    midY = 576
    pyautogui.dragTo(midX, midY, 0.3, button='left')
    print("drag2mid")

def resetMouse():
    pyautogui.moveTo(0, 0)