# Input: string
# Output: integer (score)
# Empty and none input possible
# Make sure non letter strings don't get scored (include \)
# Case insensitive

# Data structure: collection to keep the letter scores

# Algorithm
# for letter in the word, find the corresponding value and add it to the word score
import re

class Scrabble:
    SCORES = {
        'A': 1,
        'E': 1,
        'I': 1,
        'O': 1,
        'U': 1,
        'L': 1,
        'N': 1,
        'R': 1,
        'S': 1,
        'T': 1,
        'D': 2,
        'G': 2,
        'B': 3,
        'C': 3,
        'M': 3,
        'P': 3,
        'F': 4,
        'H': 4,
        'V': 4,
        'W': 4,
        'Y': 4,
        'K': 5,
        'J': 8,
        'X': 8,
        'Q': 10,
        'Z': 10
    }

    def __init__(self, word):
        self.word = word.strip() if word else ''

    def score(self):
        return Scrabble.calculate_score(self.word)
    
    @classmethod
    def calculate_score(cls, word):
        if len(word) == 0:
            return 0

        word = re.sub('\s+', '', word)

        word_score = 0
        for letter in word:
            word_score += Scrabble.SCORES[letter.upper()]
        return word_score