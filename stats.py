def number_of_words(text):
    return len(text.split())

def character_frequency(text):
    freq = {}
    for char in text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def sort_character_frequency(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetical characters
            sorted_list.append({"char": char, "num": count})
        elif char in ['æ', 'â', 'ê', 'ë', 'ô']:  # Include specific extended characters
            sorted_list.append({"char": char, "num": count})

    def sort_key(item):
        return item["num"]

    sorted_list.sort(key=sort_key, reverse=True)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()