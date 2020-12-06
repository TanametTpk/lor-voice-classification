from .abstract.Actions import Actions
from .controllers.gameController import resetMouse

class ResetMouseAction(Actions):
    def __init__(self):
        super().__init__(["reset", "รีเซ็ต"])

    def do(self, text):
        resetMouse()