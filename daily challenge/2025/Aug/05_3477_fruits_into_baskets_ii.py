class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        ans = n
        for i in range(n):
            for j in range(n):
                if baskets[j] >= fruits[i]:
                    ans -= 1
                    baskets[j] = 0
                    break
        return ans

