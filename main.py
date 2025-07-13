from stats import word_count, char_count, count_sort
import sys

def get_book_text(path):

    with open(path) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path=sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = word_count(book_contents)
    char_counts=char_count(book_contents)
    sort_count=count_sort(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #print(char_counts)
    print("--------- Character Count -------")
    #print(sort_count)
    for item in sort_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

    print(sys.argv)
    

main()