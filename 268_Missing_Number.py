# perfect O(n)
class Solution:
    def missingNumber(nums: list[int]) -> int:
        return (set([n for n in range(0, len(nums)+1)]) - set(nums)).pop()


print(Solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
