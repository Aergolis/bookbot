from stats import get_num_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print (book_text)
    total_words = get_num_words(book_text)
    print (f"{total_words} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()