
def selectCard(number):
    print("select card", number)

def getPositionPlace(place):
    if place == 'onStage':
        return 0, 0
    elif place == 'onField':
        return 0, 0

def selectEnemyChracter(number, place):
    print("select enemy character", number)

def selectFriendlyCharacter(number, place):
    print("select my character", number)

def selectCharacter(number, mode='friendly', place='onStage'):
    if mode == 'friendly':
        selectFriendlyCharacter(number, place)
    elif mode == 'enemy':
        selectEnemyChracter(number, place)

def blockEnemy(number):
    print("block", number)

def endTurn():
    print("pass")

def attackAll():
    print("attack all")

def dragToMid():
    print("drag2mid")