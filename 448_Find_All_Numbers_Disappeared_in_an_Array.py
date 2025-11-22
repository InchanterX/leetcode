# fine O(n)
class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        numbers = {}
        for num in nums:
            if num not in numbers:
                numbers[num] = 1
        return [num for num in range(1, len(nums)+1) if num not in numbers]
