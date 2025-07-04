# self-solution:
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        ans = -1
        for e in d:
            if e == d[e]:
                ans = max(ans, e)
        return ans

# faster solution:
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        ans = -1
        for k, v in c.items():
            if k == v:
                ans = max(ans, k)
        return ans
