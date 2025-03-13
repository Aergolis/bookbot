

def get_num_words(num_word):
    total_words = len(num_word.split())
    return total_words
    
def get_character_count(text):
    char_dic = {}
    for char in text:
        l_char = char.lower()
        if l_char in char_dic:
            char_dic[l_char] += 1
        else:
            char_dic[l_char] = 1
    return char_dic