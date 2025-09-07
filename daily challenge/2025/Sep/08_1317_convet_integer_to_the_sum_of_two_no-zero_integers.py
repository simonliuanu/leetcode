class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        while True:
            a = randint(1, n - 1)
            if '0' not in str(a) and '0' not in str(n - a):
                return [a, n - a]
