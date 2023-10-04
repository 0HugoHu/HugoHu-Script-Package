"""CLI interface for word_counter project.
"""
import argparse


def count_words(filename):
    """
    Count words in a text file.
    input: filename (str)
    output: word_count (int)
    """
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)


def main():
    parser = argparse.ArgumentParser(description="Count words in a text file")
    parser.add_argument("filename", help="Path to the text file")
    args = parser.parse_args()
    word_count = count_words(args.filename)
    print(f"Word count: {word_count}")
