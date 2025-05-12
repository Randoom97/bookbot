import sys
from stats import get_character_count, get_word_count, transform_character_count

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()

def main():
    args = sys.argv

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = args[1]
    text = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    list_char_counts = transform_character_count(get_character_count(text))
    for char_count in list_char_counts:
        if not char_count["char"].isalpha():
            continue
        print(f"{char_count["char"]}: {char_count["num"]}")


main()