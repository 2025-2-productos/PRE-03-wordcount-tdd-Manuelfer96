
import re

def split_into_words(preprocessed_lines):
    words = []
    for line in preprocessed_lines:
        line = re.sub(r"[^\w\s]", "", line)
        words.extend(line.split())
    return words