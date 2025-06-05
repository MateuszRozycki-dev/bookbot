def countWords(book_contents):
    bookStr = str(book_contents)
    return len(bookStr.split())

def countEverything(book_contents):
    chars = {}
    lowered = book_contents.lower()
    for c in lowered:
        if c in chars:
            chars[c] += 1
        else:chars[c] =1

    return chars

def sort_on(dict):
    return dict["num"]

def niceSorting(dictionary):
    char_list = []
    for char, count in dictionary.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)

    return char_list