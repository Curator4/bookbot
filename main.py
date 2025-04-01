import sys
from stats import count_words, count_characters, sort_dictionaries

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    content = get_book_text(sys.argv[1])
    wordcount = count_words(content)
    character_count = count_characters(content)
    sorted_wordcounts = sort_dictionaries(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for dict in sorted_wordcounts:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")
main()
