"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """
        Class that recieves a path to fa list of words found in a file. It can print out the number of words on file and generate a random word from the list
    """

    def __init__(self, path):
        lines = open(path, "r")
        self.word_list = self.create_list(lines)
        print(f"{len(self.word_list)} words read.")

    def create_list(self, lines):
        """
            Generates a list with each line in the file given as an item.
        """
        return [word.strip() for word in lines]

    def random(self):
        """"Return a random word from the list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """ A Wordfinder than excludes blank lines and comments"""

    def create_list(self, lines):
        """
            Generates a list with each line in the file given as an item.
        """
        return [word.strip() for word in lines if self.is_valid(word.strip())]

    def is_valid(self, word):
        """
            returns True if word meets certian criteria
            - word is not an empty string
            - word does not start with an #

            >>> test = SpecialWordFinder("specialtest.txt")
            4 words read.

            >>> test.is_valid("Valid")
            True

            >>> test.is_valid("")
            False

            >>> test.is_valid("#Invalid")
            False
        """
        return bool(word) and not word.startswith("#")
