def get_book_text (path):
    contents = path.read()
    return contents

def count_words (text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def main ():
    count = 0
    with open("books/frankenstein.txt") as book:
        text = get_book_text(book)
        count = count_words(text)
    print(f"Found {count} total words")

main()
