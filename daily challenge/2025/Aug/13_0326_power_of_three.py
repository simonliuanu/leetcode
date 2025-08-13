# solution 1:
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 3
        x = 0
        while True:
            p = i ** x
            if p == n:
                return True
            if p > n:
                break
            x += 1
        return False

# solution 2:
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True

# double O(1) solution:
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19 % n == 0
