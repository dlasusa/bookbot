def get_num_words(input_text: str) -> int:
    word_list = input_text.split()
    word_count = len(word_list)
    return word_count

def char_count(input_text: str) -> dict:
    char_dict = dict()
    word_list = input_text.lower().split()
    for word in word_list:
        for _char in word:
            if _char in char_dict.keys():
                char_dict[_char] += 1
            else:
                char_dict[_char] = 1
    return char_dict

def sort_dict(char_count_dict: dict) -> dict:
    return dict(sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True))