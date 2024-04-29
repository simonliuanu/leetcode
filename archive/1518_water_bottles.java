// Solve by simple simulation
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ret = numBottles;
        while (numBottles >= numExchange) {
            numBottles -= numExchange;
            ret++;
            numBottles++;
        }
        return ret;
    }
}

// Solve by mathematical analysis
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        return numBottles >= numExchange ? ((numBottles - numExchange) / (numExchange - 1) + 1) + numBottles : numBottles;
    }
}
