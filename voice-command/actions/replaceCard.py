from .abstract.Actions import Actions
from .controllers.gameController import replaceCard
from .utils.extractor import extractAndGetNumber

class ReplaceCard(Actions):
    def __init__(self):
        super().__init__(["แลกใบที่", "เปลี่ยนใบที่"])

    def do(self, text):
        cardIndex = extractAndGetNumber(text)
        replaceCard(cardIndex)