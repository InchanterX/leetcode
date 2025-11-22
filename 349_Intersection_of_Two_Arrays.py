# fine+
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
