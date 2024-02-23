def main() -> None:
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    letters_dict = count_letters(book_text)    
    dict_list = convert_dict_to_list_of_dicts(letters_dict)    
    dict_list.sort(reverse= True, key=sort_on)
    print_report(dict_list, num_words, file_path)
    

def print_report(report_dict: dict, num_words: int, file_path: str) -> None:
    print(f"""--- Begin report of {file_path} ---""")
    print(f"{num_words} words found in the document\n\n")
    for entry in report_dict:
        print(f"The '{entry['letter']}' character was found {entry['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]
    
def convert_dict_to_list_of_dicts(dict: dict, include_non_alpha = False) -> list[dict]:
    dict_list = []
    for key in dict:
        if include_non_alpha:
            dict_list.append({"letter": key,"num": dict[key]})
        else:
            if key.isalpha():
                dict_list.append({"letter": key,"num": dict[key]})

    return dict_list

def get_book_text(file_path: str) -> str:
    with open(file_path) as fp:
        return fp.read()

def count_words(book_text: str) -> int:
    list_of_words = book_text.split()
    return len(list_of_words)

def count_letters(text: str) -> dict[str: int]:
    letters_dict={}
    for letter in text:
        letter = letter.lower()
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict

if __name__ == "__main__":
    main()
    
