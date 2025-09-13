# textstats.py

<<<<<<< HEAD
def read_file():
    # Open input.txt and read the text
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.read()

def get_words(text):
    # Convert to lowercase
    text = text.lower()

    # Remove common punctuation)
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    text = text.replace("'", " ")
    text = text.replace("\"", " ")
    text = text.replace(";", " ")
    text = text.replace(":", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    # \ split the text into words
    words = text.split()

    return words

def get_char_counts(text):
    # With spaces is just length of text
    with_spaces = len(text)

    # No spaces: remove space, tab, newline
    text_no_spaces = text.replace(" ", "")
    text_no_spaces = text_no_spaces.replace("\n", "")
    text_no_spaces = text_no_spaces.replace("\t", "")
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
=======
import re
from collections import Counter

def extract_words(text):
    return re.findall(r"[a-zA-Z]+", text.lower())

def compute_statistics(text):
    words = extract_words(text)
    word_count = len(words)
    unique_words = len(set(words))

    char_count_with_spaces = len(text)
    char_count_no_spaces = len(re.sub(r"\s", "", text))

    total_letters = sum(len(word) for word in words)
    avg_word_length = round((total_letters / word_count), 1) if word_count else 0.0

    word_freq = Counter(words)
    if word_freq:
        max_freq = max(word_freq.values())
        most_common_words = sorted([word for word, freq in word_freq.items() if freq == max_freq])
    else:
        max_freq = 0
        most_common_words = []

    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "char_with_spaces": char_count_with_spaces,
        "char_no_spaces": char_count_no_spaces,
        "avg_word_length": avg_word_length,
        "most_common_words": most_common_words,
        "most_common_freq": max_freq
    }

>>>>>>> 364b67a7420bed0879ee7964670d5026557eb76a
