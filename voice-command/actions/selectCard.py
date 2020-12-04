from .abstract.Actions import Actions
from .controllers.gameController import selectCard
from .utils.extractor import extractAndGetNumber

class SelectCardAction(Actions):
    def __init__(self):
        super().__init__([
            "เลือกไพ่ใบที่",
            "เลือกใบที่",
            "เลือกไพ่ที่",
            "เอาไพ่ที่",
            "เอาไพ่ใบที่",
            "เอาไพ่ที่",
            "เอาใบที่",
            "ไพ่ที่",
            "ใบที่"
        ])

    def do(self, text):
        cardIndex = extractAndGetNumber(text)
        selectCard(cardIndex)