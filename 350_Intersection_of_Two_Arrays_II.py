# fine O(n + m)
class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        numbers1 = {}
        for num in nums1:
            if num not in numbers1:
                numbers1[num] = 1
            else:
                numbers1[num] += 1
        numbers2 = {}
        for num in nums2:
            if num not in numbers2:
                numbers2[num] = 1
            else:
                numbers2[num] += 1

        output = []
        for key in numbers1.keys():
            if key in numbers2:
                output += [key]*min(numbers1[key], numbers2[key])
        return output


# print(Solution.intersect([1, 2, 2, 1], [2, 2]))
