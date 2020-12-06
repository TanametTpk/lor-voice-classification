from actions.attackAll import AttackAllAction
from actions.endTurn import EndTurnAction
from actions.selectCard import SelectCardAction
from actions.selectCharacter import SelectCharacterAction
from actions.useCard import UseCardAction
from actions.selectEnemyCharacter import SelectEnemyCharacterAction
from actions.resetMouse import ResetMouseAction
from actions.selectNexus import SelectNexusAction

def matchAction(text, actions):
    orders = []

    for action in actions:
        isMatch, word = action.isMatch(text)

        if not isMatch:
            continue

        idx = text.lower().index(word.lower())
        if idx > -1:
            orders.append({
                "action": action,
                "idx": idx
            })

    orders.sort(key=lambda x: x["idx"])
    return orders

def contextSelection(text):
    actions = [
        SelectCardAction(),
        SelectCharacterAction(),
        SelectEnemyCharacterAction(),
        UseCardAction(),
        AttackAllAction(),
        EndTurnAction(),
        ResetMouseAction(),
        SelectNexusAction()
    ]
    orders = matchAction(text, actions)

    for i in range(len(orders)):
        order = orders[i]
        endContext = len(text)

        if i < len(orders) - 1:
            endContext = orders[i+1]["idx"]

        currentContext = text[order["idx"]:endContext]
        order["action"].do(currentContext)