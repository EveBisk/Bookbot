import os


def open_book(path: str):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def word_count(text: str):
    return len(text.split())


def character_count(text: str):
    count_dict = {}
    for cha in text.lower():
        if cha not in count_dict.keys():
            count_dict[cha] = 1
        else:
            count_dict[cha] += 1

    return count_dict


def dictionary_sort(dict):
    unsorted_list = [{"char": k, "value": dict[k]} for k in dict.keys()]
    sorted = unsorted_list.sort(reverse=True, key=lambda x: x["value"])
    print(sorted)
    return unsorted_list


def main():
    filepath = "books/frankenstein.txt"

    content = open_book(filepath)
    print("Printing the book report:")
    print(content)
    print("-" * 20)

    words = word_count(content)
    print(f"The word count is {words}")

    character_dict = dictionary_sort(character_count(content))
    for entry in character_dict:
        if not entry["char"].isalpha():
            continue
        print(f"The {entry['char']} character was found {entry['value']} times \n")


main()
