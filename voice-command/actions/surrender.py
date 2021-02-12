from .abstract.Actions import Actions
from .controllers.gameController import surrender

class SurrenderAction(Actions):
    def __init__(self):
        super().__init__(["ยอมแพ้"])

    def do(self, text):
        surrender()