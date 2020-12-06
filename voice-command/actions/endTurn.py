from .abstract.Actions import Actions
from .controllers.gameController import endTurn

class EndTurnAction(Actions):
    def __init__(self):
        super().__init__(["จบ", "skip", "ข้าม", "ผ่าน", "pass", "ok", "โอเคร"])

    def do(self, text):
        endTurn()