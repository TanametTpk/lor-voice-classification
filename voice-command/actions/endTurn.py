from .abstract.Actions import Actions
from .controllers.gameController import endTurn

class EndTurnAction(Actions):
    def __init__(self):
        super().__init__(["จบ", "skip", "ผ่าน", "pass", "ok", "โอเค"])

    def do(self, text):
        endTurn()