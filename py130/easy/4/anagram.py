# class Anagram:

# Input: word (string) and a list of words (strings)
# Output: List of words (strings), can be empty
# No errors raised by the constructor

# Algorithm
# Do I have to find all possible anagrams or just check?
# For each word in the list provided
#  If they don't have the same length next iteration
#  Sort the input word and the candidate and compare them
#   If they are the same, append to the result list

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        sorted_word = ''.join(sorted(self.word))
        anagrams = []
        for candidate in candidates:
            if ''.join(sorted(candidate.lower())) == sorted_word and self.word.lower() != candidate.lower():
                anagrams.append(candidate)
        return anagrams
    
detector = Anagram("Orchestra")
print(detector.match(["cashregister", "Carthorse", "radishes"]))
