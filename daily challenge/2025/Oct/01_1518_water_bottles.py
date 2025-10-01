# simulation:
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            ans += numExchange
            numBottles -= numExchange - 1
        return ans + numBottles

# math:
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
