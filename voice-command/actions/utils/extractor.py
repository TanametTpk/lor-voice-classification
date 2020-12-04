def string2Number(text):
    textNumber = text.replace(' ', '')
    if (not textNumber.isnumeric()):
        return -1

    return int(textNumber)

def extractNumberFromText(text):
    try:
        idx = text.index("ที่") + 3
        return text[idx:]
    except:
        return "0"

def getOnlyNumber(text):
    textNumber = ""
    for t in text:
        if t.isdigit():
            textNumber += t
        elif len(textNumber) > 0:
            break

    return textNumber

def extractAndGetNumber(text):
    numberText = extractNumberFromText(text)
    onlyNumber = getOnlyNumber(numberText)
    return string2Number(onlyNumber)

def isMatch(text, words):
    for word in words:
        if word in text.lower():
            return True, word

    return False, ""