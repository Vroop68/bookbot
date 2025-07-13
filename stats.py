def word_count(book_text):
    words = str.split(book_text)
    count = len(words)
    return count

def char_count(book_text):
    counts = {}
    for char in book_text:
        char = char.lower()
        if char.isalpha():
            if char in counts:
                counts[char]+=1
            else:
                counts[char] = 1
    return counts

def sort_num(item):
    return item["num"]

def count_sort(book_dict):
    book_list = []
    for char, num in book_dict.items():
        book_list.append({"char": char, "num": num})

    book_list.sort(key=sort_num, reverse=True)
    return book_list