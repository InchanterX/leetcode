# fine
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(s: str, t: str) -> bool:
        available_letters = {}
        for letter in s:
            if letter in available_letters:
                available_letters[letter] += 1
            else:
                available_letters[letter] = 1

        anagram_letters = {}
        for letter in t:
            if letter in anagram_letters:
                anagram_letters[letter] += 1
            else:
                anagram_letters[letter] = 1

        len_available = 0
        len_anagram = 0
        is_equal = True
        for key in available_letters.keys():
            len_available += available_letters[key]
        for key in anagram_letters.keys():
            len_anagram += anagram_letters[key]
            if key not in available_letters:
                is_equal = False
                break
            elif available_letters[key] != anagram_letters[key]:
                is_equal = False
                break

        if (not is_equal) or (len_anagram != len_available):
            return False
        else:
            return True


print(Solution.isAnagram("a", "b"))
