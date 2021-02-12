from .abstract.Actions import Actions
from .controllers.gameController import cancelSpell

class CancelSpellAction(Actions):
    def __init__(self):
        super().__init__(["ยกเลิก"])

    def do(self, text):
        cancelSpell()