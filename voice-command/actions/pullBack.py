from .abstract.Actions import Actions
from .controllers.gameController import pullBack

class PullBack(Actions):
    def __init__(self):
        super().__init__(["กลับ"])

    def do(self, text):
        pullBack()