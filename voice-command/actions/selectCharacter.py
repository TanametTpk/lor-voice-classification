from .abstract.Actions import Actions
from .controllers.gameController import selectCharacter, blockEnemy, dragToMid
from .utils.extractor import extractAndGetNumber, isMatch

class SelectCharacterAction(Actions):
    def __init__(self):
        super().__init__(["เลือกตัวที่", "เอาตัวที่"])
        self.attackWords = ["โจมตี", "ตี", "attack"]
        self.blockWords = ["ป้องกัน", "กัน", "block", "บล็อค"]

    def checkWordMatch(self, text, mode='attack'):
        words = self.attackWords
        if mode == 'block':
            words = self.blockWords
        return isMatch(text, words)

    def isContinusWordAction(self, text):
        isAttack, attackWord = self.checkWordMatch(text, mode='attack')
        isBlock, blockWord = self.checkWordMatch(text, mode='block')

        if not (isAttack or isBlock):
            return False, "", ""

        if isAttack:
            return True, "attack", attackWord
        else:
            return True, "block", blockWord

    def splitContext(self, text, word):
        splitIdx = text.index(word)
        return [ text[:splitIdx], text[splitIdx:] ]

    def do(self, text):
        isRight, mode, word = self.isContinusWordAction(text)
        place = "onStage"

        if "สนาม" in text:
            place = "onField"

        if not isRight:
            charIndex = extractAndGetNumber(text)
            selectCharacter(charIndex, mode='friendly', place=place)
            return

        characterPart, actionPart = self.splitContext(text, word)
        charIndex = extractAndGetNumber(characterPart)
        selectCharacter(charIndex, mode='friendly', place=place)

        if mode == 'block':
            enemyIndex = extractAndGetNumber(actionPart)
            blockEnemy(enemyIndex)
        elif mode == 'attack':
            dragToMid()