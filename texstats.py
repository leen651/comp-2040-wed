# textstats.py

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

