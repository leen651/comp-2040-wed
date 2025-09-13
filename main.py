# main.py


import re  

def read_file():
    # Open input.txt and read the text
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.read()

def get_words(text):
    # Convert to lowercase
    text = text.lower()

    # Remove common punctuation (basic way)
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("'", " ")
    text = text.replace("-", " ")
    

    # split the text into words
    words = text.split()

    return words

def get_char_counts(text):
    # With spaces is just length of text
    with_spaces = len(text)

    # No spaces: remove space, tab, newline
    text_no_spaces = text.replace(" ", "")
    no_spaces = len(text_no_spaces)

    return with_spaces, no_spaces

def get_average_word_length(words):
    if len(words) == 0:
        return 0.0

    total_letters = 0
    for word in words:
        total_letters += len(word)

    return total_letters / len(words)

def get_most_common_words(words):
    if len(words) == 0:
        return [], 0

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find highest count
    max_count = 0
    for word in word_counts:
        if word_counts[word] > max_count:
            max_count = word_counts[word]

    # Find all words with that count
    most_common = []
    for word in word_counts:
        if word_counts[word] == max_count:
            most_common.append(word)

    # Sort them
    most_common.sort()

    return most_common, max_count

def write_output(stats):
    word_count, unique_words, chars_with, chars_without, avg_length, common_words, common_count = stats

    if len(common_words) > 0:
        common_words_line = ", ".join(common_words)
        line6 = f"Most common word(s): {common_words_line} ({common_count})"
    else:
        line6 = "Most common word(s): (0)"

from textstats import compute_statistics

    lines = [
        f"Word count: {word_count}",
        f"Unique words: {unique_words}",
        f"Characters (with spaces): {chars_with}",
        f"Characters (no spaces): {chars_without}",
        f"Average word length: {avg_length:.1f}",
        line6
    ]

    for line in lines:
        print(line)

    with open("output.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

def main():
    text = read_file()
    words = get_words(text)

    word_count = len(words)
    unique_words = len(set(words))
    avg_length = get_average_word_length(words)
    chars_with, chars_without = get_char_counts(text)
    common_words, common_count = get_most_common_words(words)

    stats = (word_count, unique_words, chars_with, chars_without, avg_length, common_words, common_count)

    write_output(stats)

if __name__ == "__main__":
    main()
