import sys
from pathlib import Path

from stats import char_count, get_num_words, sort_dict


def get_book_text(input_path: str) -> str:
    print(f'Analyzing book found at {input_path}...')
    with Path(input_path).open(mode='r') as f:
        book_text = f.read()
        return book_text


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print('============ BOOKBOT ============')
    book_str = get_book_text(sys.argv[1])
    wc = get_num_words(input_text=book_str)
    character_dict = char_count(input_text = book_str)
    print('----------- Word Count ----------')
    print(f'Found {wc} total words')
    print('--------- Character Count -------')
    sorted_char_count = sort_dict(char_count_dict=character_dict)
    for item in sorted_char_count.items():
        print(f'{item[0]}: {item[1]}')
    print('============= END ===============')

main()