# fine O(n)
class Solution:
    # def firstUniqChar(self, s: str) -> int:
    def firstUniqChar(s: str) -> int:
        letters = {}
        for i, letter in enumerate(s):
            if letter not in letters.keys():
                letters[letter] = [1, i]
            else:
                letters[letter][0] += 1
        for letter in letters.keys():
            if letters[letter][0] == 1:
                return letters[letter][1]
        return -1
