# perfect O(n^2)
class Solution:
    def generate(self, numRows):
        res = [[1]]
        for _ in range(1, numRows):
            prev = res[-1]
            row = [1]
            for i in range(1, len(prev)):
                row.append(prev[i] + prev[i - 1])
            row.append(1)
            res.append(row)
        return res
