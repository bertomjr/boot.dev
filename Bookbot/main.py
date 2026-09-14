import sys
from stats import get_num_words, get_char_count, chars_dict_to_sorted_list


def get_book_text(filepath:str ) -> str:
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def print_report(filepath:str, word_count: int, sorted_char_count: list[tuple[str, int]]):
    print(f'''============ BOOKBOT ============
Analyzing book found at {filepath}...''')
    print(f'''----------- Word Count ----------
Found {word_count} total words''')
    print("--------- Character Count -------")
    for char, count in sorted_char_count:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = chars_dict_to_sorted_list(char_count)
    print_report(filepath, word_count, sorted_char_count)

main()