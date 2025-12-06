
from typing import Counter


def count_words(words):
    """
    Counts the occurrences of each word in the given list.

    Parameters:
        words (list of str): The list of words to count.

    Returns:
        Counter: A Counter object mapping words to their counts.
    """
    return Counter(words)
