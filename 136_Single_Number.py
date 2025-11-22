# perfect
from typing import List


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(nums: List[int]) -> int:
        not_paired = {}
        for i in range(len(nums)):
            if not not_paired.get(nums[i]):
                not_paired[nums[i]] = "1"
            else:
                del not_paired[nums[i]]
        for key in not_paired.keys():
            return key


print(Solution.singleNumber([1, 2, 1, 4, 2]))
