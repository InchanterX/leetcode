class Solution:
    # def firstUniqChar(self, s: str) -> int:
    def firstUniqChar(s: str) -> int:
        letters = {}
        for letter in s:
            if letter not in letters.keys():
                letters[letter] = 1
            else:
                letters[letter] += 1
