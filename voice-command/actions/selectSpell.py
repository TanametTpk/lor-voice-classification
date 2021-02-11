from .abstract.Actions import Actions
from .controllers.gameController import selectSpell

class SelectSpellAction(Actions):
    def __init__(self):
        super().__init__(["สกิล", "skill", "เวทมนต์", "เวทมนตร์", "spell"])

    def do(self, text):
        selectSpell()