# can't pass the time limit because code is bad
class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    def subarraySum(nums: list[int], k: int) -> int:
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[i-1] + nums[i])
        count = 0
        for i in range(len(prefix_sums)):
            if prefix_sums[i] == k:
                count += 1

        for i in range(len(prefix_sums)):
            for j in range(i+1, len(prefix_sums)):
                if (prefix_sums[j] - prefix_sums[i]) == k:
                    count += 1
        return count


print(Solution.subarraySum([1, 2, 3], 3))
