# fine O(n)
class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        quantity = {}
        for num in nums:
            if num not in quantity:
                quantity[num] = 1
            else:
                quantity[num] += 1
        output = []
        for i in range(k):
            max_el = max(quantity, key=quantity.get)
            output.append(max_el)
            del quantity[max_el]
        # return quantity.pop(max(quantity.values()))
        return output


print(Solution.topKFrequent([4, 1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
