from typing import List


class Solution:
    # Leetcode option
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(nums: List[int]) -> int:
        p1 = 0
        p2 = 1
        k = 1
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                print(1, p1, p2, nums)
                p2 += 1
            elif nums[p1] > nums[p2]:
                p2 += 1
            else:
                nums[p1+1] = nums[p2]
                print(2, p1, p2, nums)
                k += 1
                p1 += 1
                p2 = p1+1
        return k


print(Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
