# fine, better to get rid of sorting
class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(nums: list[int]) -> bool:
        set_nums = set(nums)
        print(sorted(list(set_nums)), sorted(nums))
        if sorted(list(set_nums)) == sorted(nums):
            return False
        return True


print(Solution.containsDuplicate([1, 5, -2, -4, 0]))
