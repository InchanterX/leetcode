# fine O(n)
class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
        checked = {}
        for i, num in enumerate(nums):
            if num in checked and i - checked[num] <= k:
                return True
            else:
                checked[num] = i
        return False
