class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = ans = numBottles
        while emptyBottles >= numExchange:
            ans += 1
            emptyBottles -= numExchange - 1
            numExchange += 1
        return ans
