# self solution:
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n & 1 == 1:
            ans.append(0)
        for i in range(1, n // 2 + 1):
            ans += [i, -i]
        return ans
