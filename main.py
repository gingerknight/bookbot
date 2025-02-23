# Python file to read books from a file
# Python Imports
import sys

# Local Imports
from stats import find_num_words, char_frequency, sort_dict

def get_book_text(book: str):
    with open(book) as f:
        contents = f.read()
    return contents


def main():
    
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    # book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}")

    book_contents = get_book_text(book_path)
    words_in_book = find_num_words(book_contents)
    print("----------- Word Count ----------")
    print(words_in_book)
    
    print("--------- Character Count -------")
    char_dict = char_frequency(book_contents)
    
    sorted_tuple = sort_dict(char_dict) 
    for item in sorted_tuple:
        print(f"{item[0]}: {item[1]}")


main()
