import pyautogui
pyautogui.displayMousePosition()

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

    pyautogui.moveTo(x, y)

def selectCard(selectIdx, max):
    MAX = 1449
    MIN = 480
    CARDWIDTH = 165

    x = 960
    y = 1040

    calculatePosition(MIN, MAX, CARDWIDTH, x, y, selectIdx, max)

def selectCharacter(selectIdx, max):
    MAX = 1404
    MIN = 513
    CARDWIDTH = 155

    x = 960
    y = 900

    calculatePosition(MIN, MAX, CARDWIDTH, x, y, selectIdx, max)

def selectField(selectIdx, max):
    MAX = 1538
    MIN = 379
    CARDWIDTH = 280

    x = 960
    y = 708
    calculatePosition(MIN, MAX, CARDWIDTH, x, y, selectIdx, max)

# selectCard(3, 5)
# selectField(2, 2)

# selectCharacter(2, 2)