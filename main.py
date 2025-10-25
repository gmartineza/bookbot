import stats, sys



def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(file_path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(stats.get_num_words(text))

    print("--------- Character Count -------")
    for item in stats.sorted_dicts(text):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()