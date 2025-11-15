import sys
from stats import count_words
from stats import count_non_words
from stats import sort_chars

def get_book_text (path):
    contents = path.read()
    return contents

def character_read_out (charList):
    for entry in charList:
        currentDict = entry
        print(f"{currentDict["char"]}: {currentDict["num"]}")

def main ():
    try:
        with open(sys.argv[1]) as book:
            # Get full text of file.
            text = get_book_text(book)

            # Get total word count.
            wordCount = count_words(text)

            # Get count of all characters as dictionary.
            charCount = count_non_words(text)

            # Sort charCount dictionary into a list of seperate dictionaries.
            sortedChars = sort_chars(charCount)

        print(
            "============ BOOKBOT ============\n" + 
            f"Analyzing book found at {book.name}...\n" + 
            "----------- Word Count ----------\n"
            f"Found {wordCount} total words\n" + 
            "--------- Character Count -------\n"
            )
        print(character_read_out(sortedChars))
        print("============= END ===============")
    except:
        print("Usage: python3 main.py <path_to_book>")

    #print(f"Found {wordCount} total words")
    #print(sort_chars(charCount))

main()
