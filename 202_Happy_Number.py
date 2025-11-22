# perfect O(log(n))
class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        while n not in checked:
            checked.add(n)
            result = 0
            while n:
                num = n % 10
                result += num ** 2
                n = n // 10
            if result == 1:
                return True
            n = result
        return False
