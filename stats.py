from typing import Dict, Tuple

def find_num_words(book_text: str) -> str:

    book_string_split = book_text.split() # split string by space
    num_words = len(book_string_split)
    # print(num_words)
    return f"Found {num_words} total words"


def char_frequency(book_text: str) -> Dict:
    """
        Counts the freq of characters of the alphabet
        in the book text
    Returns: Dict
    """
    alpha_dict = {}
    book_lower_string = book_text.lower()
    for char in book_lower_string:
        if char.isalpha():
            if char not in alpha_dict:
                alpha_dict[char] = 1
            elif char in alpha_dict:
                alpha_dict[char] += 1

    return alpha_dict

def get_value(item: Tuple[str,int]) -> int:
    """
    Helper function to retrieve the value from a tuple
    """
    return item[1]


def sort_dict(freq_dict: dict) -> Dict:
    """
    Sorts a dictionary of chars by greatest to least
    """
    return sorted(freq_dict.items(), key=get_value, reverse=True)
