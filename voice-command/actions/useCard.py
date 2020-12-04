from .abstract.Actions import Actions
from .controllers.gameController import dragToMid

class UseCardAction(Actions):
    def __init__(self):
        super().__init__(["ลง", "ใช้"])

    def do(self, text):
        dragToMid()