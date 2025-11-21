

class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(nums: list[int]) -> bool:
        set_nums = set(nums)
        if list(set_nums) == nums:
            return False
        return True


print(Solution.containsDuplicate([1, 2, 3, 4]))
