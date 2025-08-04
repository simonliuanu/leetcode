class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        l = 0
        d = defaultdict(int)
        for r, fruit in enumerate(fruits):
            d[fruit] += 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans

