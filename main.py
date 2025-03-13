from stats import get_num_words
from stats import get_character_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    total_words = get_num_words(book_text)
    print (f"{total_words} words found in the document")
    char_count = get_character_count(book_text)
    for char, count in char_count.items():
        print(f"'{char}': {count}")
    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()