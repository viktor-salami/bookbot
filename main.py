from stats import count_words
from stats import count_non_words

def get_book_text (path):
    contents = path.read()
    return contents

def main ():
    with open("books/frankenstein.txt") as book:
        text = get_book_text(book)
        wordCount = count_words(text)
        charCount = count_non_words(text)
    print(f"Found {wordCount} total words")
    print(f"Here is the frequency of the following characters: {charCount}")

main()
