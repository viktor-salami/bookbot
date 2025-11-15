def count_words (text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_non_words (text):
    lowerCase = list(text.lower())
    charCount = {}

    for char in lowerCase:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    return charCount

def sort_on (items):
    return items["num"]


def sort_chars (charDict):
    sortedChars = []
    
    # create a list of dictionaries where each dict contains two key value pairs:
    # one for the character (alphanumeric only), one for its frequency.
    # I.E. [{char: 'e', num: 500}, {char: 'c', num: 250}]
    for char, count in charDict.items():
        currentDict = {}
        currentDict[char] = (count)
        for key, value in currentDict.items():
            charNum = {}
            if key.isalpha():
                charNum["char"] = key
                charNum["num"] = value
                sortedChars.append(charNum)
            else:
                continue
    
    sortedChars.sort(reverse=True, key=sort_on)
    return sortedChars

