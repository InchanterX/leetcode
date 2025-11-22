# fine+ O(n)
class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    def longestConsecutive(nums: list[int]) -> int:
        nums = set(nums)
        max_length = 0
        for el in nums:
            if el-1 not in nums:
                length = 1
                while el+length in nums:
                    length += 1
                max_length = max(max_length, length)
        return max_length
