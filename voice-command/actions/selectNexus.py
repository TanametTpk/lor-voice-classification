from .abstract.Actions import Actions
from .controllers.gameController import selectNexus, selectOnField

class SelectNexusAction(Actions):
    def __init__(self):
        super().__init__(["ตัวเอง", "ฝั่งศัตรู"])

    def do(self, text):
        if "ตัวเอง" in text:
            selectNexus(side="my")
        else:
            selectNexus(side="enemy")
