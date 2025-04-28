def count_words(text):
    words = text.split()
    return len(words)

def count_used_characters(text):
    text = text.lower()
    char_counts = {}
    for i in range(0, len(text)):
        char = text[i]
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_dict(dict):
    keys = list(dict)
    max = float("-inf")
    max_key = None
    sorted = {}
    while len(dict) > 0:
        for key in keys:
            if dict[key] > max:
                max = dict[key]
                max_key = key
        sorted[max_key] = dict[max_key]
        dict.pop(max_key)
        keys = list(dict)
        max = float("-inf")
        max_key = None
    return sorted
