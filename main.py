from stats import countWords, countEverything, niceSorting
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_content = get_book_text(filepath)
    new_words = countWords(book_content)
    countedEverything = countEverything(book_content)

    
    sorted =niceSorting(countedEverything)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {new_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()