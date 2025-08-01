class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter(basket1 + basket2)
        min_val = min(cnt)
        for i in cnt:
            if cnt[i] % 2 == 1:
                return -1

        d = Counter(basket1)
        d.subtract(basket2)

        A = []
        B = []
        for i, j in d.items():
            if j > 0:
                A += [i] * (j // 2)
            elif j < 0:
                B += [i] * (-j // 2)

        A.sort()
        B.sort(reverse=True)
        ans =  0
        for a, b in zip(A, B):
            ans += min(min(a, b), 2 * min_val)

        return ans

