from .abstract.Actions import Actions
from .controllers.gameController import attackAll

class AttackAllAction(Actions):
    def __init__(self):
        super().__init__(["โจมตีทั้งหมด", "ตีทั้งหมด", "direct attack"])

    def do(self, text):
        attackAll()