
class Actions:
    def __init__(self, words):
        self.words = words

    def isMatch(self, text):
        for word in self.words:
            if word in text.lower():
                return True, word

        return False, ""

    def do(self, data):
        pass