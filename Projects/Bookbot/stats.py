# Get the number of words in the book text
def get_num_words(book_text:str) -> int:
    word_count = len(book_text.split())
    return word_count

# Get the count of each character in the book text
def get_char_count(book_text:str) -> dict[str, int]:
    char_count = {}
    for char in book_text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Helper function to sort a tuple of (character, count) based on the count
def sort_on(data: tuple[str, int]) -> int:
    return data[1]

# Convert the character count dictionary to a sorted list of tuples
def chars_dict_to_sorted_list( char_count: dict[str, int]) -> list[tuple[str, int]]:
    sorted_char_count = []
    for char, count in char_count.items():
        sorted_char_count.append((char, count))
    sorted_char_count.sort(key=sort_on, reverse=True)
    return sorted_char_count