

import os


def write_word_counts(output_folder, word_counts):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_file_path, "w", encoding="utf-8") as file:
        for word, count in word_counts.items():
            file.write(f"{word}\t{count}\n")