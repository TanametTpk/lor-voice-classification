import pyautogui
from .ocr.core import getResources as coreGetResorces
import time

pyautogui.FAILSAFE = False

def getResources():
    x, y = pyautogui.position()
    resetMouse()
    time.sleep(0.3)
    resources = coreGetResorces()
    pyautogui.moveTo(x, y)

    return resources

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

def getCardPosition(selectIdx, max, refPosition):
    selectIdx = selectIdx - 1
    if selectIdx < 0 or len(refPosition) < 1:
        return 0, 0

    if len(refPosition) <= selectIdx:
        selectIdx = len(refPosition) - 1

    [x, y, r] = refPosition[selectIdx]

    return x + r, y + r

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

def selectSpell():
    pyautogui.click(x=958, y=534) 

def selectCard(number):
    resources = getResources()
    print("select card", number)
    x, y = getCardPosition(number, resources["cards"], resources["cardPositions"])
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

def selectMyMonsterOnField(number):
    resources = getResources()
    x, y = getFieldPosition(number, resources["myField"])
    pyautogui.click(x=x, y=y)

def selectEnemyMonsterOnField(number):
    resources = getResources()
    x, y = getFieldPosition(number, resources["enemyField"])
    pyautogui.click(x=x, y=y)

def selectCharacter(number, mode='friendly', place='onStage'):
    if mode == 'friendly' and place == "onStage":
        selectFriendlyCharacter(number, place)
    elif mode == 'enemy' and place == "onStage":
        selectEnemyChracter(number, place)
    elif mode == 'friendly' and place == "onField":
        selectMyMonsterOnField(number)
    elif mode == 'enemy' and place == "onField":
        selectEnemyMonsterOnField(number)

def dragToPosition(x, y):
    pyautogui.dragTo(x, y, 0.3, button='left')
    print("drag2", x, y)

def pullEnemy(number):
    resources = getResources()
    x, y = getFieldPosition(number, resources["myField"])
    dragToPosition(x, y - 293)
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
    print("reset")

def selectNexus(side="my"):
    x = 238
    y = 659
    if side == "enemy":
        y = 417
    pyautogui.click(x=x, y=y) 
    print("select " + side + " nexus")

def pullBack():
    dragToPosition(1000, 1000)
    resetMouse()

def replaceCard(selectIdx):
    xTargets = [527, 811, 1079, 1353]
    y = 543

    selectIdx = selectIdx - 1
    if not (selectIdx > -1 and selectIdx < 4):
        return

    x = xTargets[selectIdx]    
    pyautogui.click(x=x, y=y)

def surrender():
    pyautogui.click(x=1852, y=52)
    time.sleep(0.1)
    pyautogui.click(x=918, y=893)
    time.sleep(0.1)
    pyautogui.click(x=1102, y=609)

def cancelSpell():
    # pyautogui.rightClick()
    selectSpell()
    pullBack()