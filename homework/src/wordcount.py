

import argparse
import os
import re
from collections import defaultdict, Counter
from homework.src._internals.read_all_lines import read_all_lines


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder containing files to process.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def preprocess_lines(lines):
    return [line.strip().lower() for line in lines]


def split_into_words(preprocessed_lines):
    words = []
    for line in preprocessed_lines:
        line = re.sub(r"[^\w\s]", "", line)
        words.extend(line.split())
    return words




def count_words(words):
    """
    Counts the occurrences of each word in the given list.

    Parameters:
        words (list of str): The list of words to count.

    Returns:
        Counter: A Counter object mapping words to their counts.
    """
    return Counter(words)

def write_word_counts(output_folder, word_counts):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_file_path, "w", encoding="utf-8") as file:
        for word, count in word_counts.items():
            file.write(f"{word}\t{count}\n")


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)
