#!/usr/bin/env python3

import sys

from stats import get_num_words, get_char_count, get_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def usage():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(book):
    num_words = get_num_words(get_book_text(book))
    char_count = get_char_count(get_book_text(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in get_report(char_count):
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


print(sys.argv)
if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    usage()
