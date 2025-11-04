from stats import count_words

def get_book_text (path):
    contents = path.read()
    return contents

def main ():
    count = 0
    with open("books/frankenstein.txt") as book:
        text = get_book_text(book)
        count = count_words(text)
    print(f"Found {count} total words")

main()
