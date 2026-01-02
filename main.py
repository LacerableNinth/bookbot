#!/usr/bin/env python3

from stats import get_num_words, get_char_count, get_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book = "books/frankenstein.txt"
    num_words = get_num_words(get_book_text(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_count = get_char_count(get_book_text("books/frankenstein.txt"))
    for item in get_report(char_count):
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
