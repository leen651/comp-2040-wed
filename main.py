# main.py

from textstats.py import compute_statistics

def format_output(stats):
    lines = [
        f"Word count: {stats['word_count']}",
        f"Unique words: {stats['unique_words']}",
        f"Characters (with spaces): {stats['char_with_spaces']}",
        f"Characters (no spaces): {stats['char_no_spaces']}",
        f"Average word length: {stats['avg_word_length']:.1f}",
    ]

    if stats["most_common_words"]:
        words = ", ".join(stats["most_common_words"])
        lines.append(f"Most common word(s): {words} ({stats['most_common_freq']})")
    else:
        lines.append(f"Most common word(s): ({stats['most_common_freq']})")

    return lines

def main():
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    stats = compute_statistics(text)
    output_lines = format_output(stats)

    for line in output_lines:
        print(line)

    with open("output.txt", "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    main()



