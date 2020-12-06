from .abstract.Actions import Actions
from .controllers.gameController import selectCharacter, pullEnemy, dragToMid
from .utils.extractor import extractAndGetNumber, isMatch

class SelectEnemyCharacterAction(Actions):
    def __init__(self):
        super().__init__([
            "เลือกฝั่งตรงข้ามตัวที่",
            "เลือกศัตรูตัวที่",
            "เอาฝั่งตรงข้ามตัวที่",
            "เอาศัตรูตัวที่",
            "เลือกคู่แข่งตัวที่",
            "เอาคู่แข่งตัวที่",
        ])
        self.pullWords = ["ลาก", "ดึง", "มา"]

    def checkWordMatch(self, text, mode='pull'):
        words = self.pullWords
        return isMatch(text, words)

    def isContinusWordAction(self, text):
        isPull, pullWord = self.checkWordMatch(text, mode='pull')

        if not (isPull):
            return False, "", ""

        return True, "pull", pullWord

    def splitContext(self, text, word):
        splitIdx = text.index(word)
        return [ text[:splitIdx], text[splitIdx:] ]

    def do(self, text):
        isRight, mode, word = self.isContinusWordAction(text)

        if not isRight:
            charIndex = extractAndGetNumber(text)
            selectCharacter(charIndex, mode='enemy', place='onStage')
            return

        characterPart, actionPart = self.splitContext(text, word)
        charIndex = extractAndGetNumber(characterPart)
        selectCharacter(charIndex, mode='enemy', place='onStage')

        if mode == 'pull':
            myMonsterIndex = extractAndGetNumber(actionPart)
            pullEnemy(myMonsterIndex)