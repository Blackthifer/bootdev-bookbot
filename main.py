from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    return "Faulty filepath"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_used_characters(text)
    sorted_counts = sort_dict(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for count in sorted_counts:
        print(f"{count}: {sorted_counts[count]}")
    print("============= END ===============")

main()