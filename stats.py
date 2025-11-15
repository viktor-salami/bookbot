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
