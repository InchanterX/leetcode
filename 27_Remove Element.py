# fine
from typing import List


class Solution:
    # Leetcode version
    # def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(nums: List[int], val: int) -> int:
        p1 = 0
        k = 0
        p2 = len(nums) - 1
        while p1 != p2:
            if nums[p1] != val:
                k += 1
                p1 += 1
            elif nums[p2] == val:
                p2 -= 1
            elif nums[p1] == val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                k += 1
                p1 += 1
                p2 -= 1
        return k+1


print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
