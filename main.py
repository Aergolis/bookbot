from stats import get_num_words         # Importování funkcí z jiného souboru
from stats import get_character_count   # Importování funkcí z jiného souboru
from stats import sort_char_by_count    # Importování funkcí z jiného souboru
import sys                              # Importování knihovny sys


def main():
    # filepath = input("Enter the path to the book you want to analyze: ") Jiné řešení

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")  # Pokud není zadán argument, vypíše se nápověda
        sys.exit(1)
    else:
        filepath = sys.argv[1]      # Získání cesty k souboru z argumentů

    book_text = get_book_text(filepath)     # Získání textu z knihy
    total_words = get_num_words(book_text)  # Získání počtu slov


    char_count = get_character_count(book_text)     # Získání počtu znaků
    sorted_chars = sort_char_by_count(char_count)   # Seřazení znaků podle počtu výskytů

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for char_info in sorted_chars:  # Výpis znaků a jejich počtu
        char = char_info["char"]        # Získání znaku
        count = char_info["count"]      # Získání počtu výskytů
        if char.isalpha():          # Pokud je znak písmeno, vypíše se
            print(f"{char}: {count}")

    print("============= END ===============")

def get_book_text(filepath):         # Funkce pro získání textu z knihy
    with open(filepath) as f:        # Otevření souboru
        file_contents = f.read()     # Přečtení obsahu souboru
    return file_contents


main()