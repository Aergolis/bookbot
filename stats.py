

def get_num_words(num_word):                # Funkce pro získání počtu slov
    total_words = len(num_word.split())     # Rozdělení textu podle mezer a získání délky
    return total_words
    
def get_character_count(text):      # Funkce pro získání počtu znaků
    char_dic = {}               # Vytvoření slovníku pro znaky
    for char in text:           # Procházení znaků v textu
        l_char = char.lower()   # Převedení do malých písmen
        if l_char in char_dic:      # Pokud znak již existuje, přičte se 1
            char_dic[l_char] += 1
        else:
            char_dic[l_char] = 1    # Jinak se vytvoří nový záznam
    return char_dic

def sort_on(dict_item):        # Funkce pro seřazení znaků podle počtu výskytů
    return dict_item["count"]       # Vrátí počet výskytů

def sort_char_by_count(char_count): # Funkce pro seřazení znaků podle počtu výskytů
    char_list = []                  # Vytvoření listu pro znaky
    for char, count in char_count.items():                  # Procházení znaků a jejich počtu
        char_list.append({"char": char, "count": count})    # Přidání znaku a jeho počtu do listu
    char_list.sort(key=sort_on, reverse=True)               # Seřazení listu podle počtu výskytů
    return char_list

