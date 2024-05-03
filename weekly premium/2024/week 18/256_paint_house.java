// Dynamic programming
class Solution {
    public int minCost(int[][] costs) {
        int cost[][] = new int[costs.length][3];

        cost[0][0] = costs[0][0];
        cost[0][1] = costs[0][1];
        cost[0][2] = costs[0][2];

        for (int i = 1; i < costs.length; i++) {
            cost[i][0] = Math.min(cost[i - 1][1], cost[i - 1][2]) + costs[i][0];
            cost[i][1] = Math.min(cost[i - 1][0], cost[i - 1][2]) + costs[i][1];
            cost[i][2] = Math.min(cost[i - 1][0], cost[i - 1][1]) + costs[i][2];
        }

        return Math.min(cost[cost.length - 1][0], Math.min(cost[cost.length - 1][1], cost[cost.length - 1][2]));
    }
}

// Dynamic programming refined
class Solution {
    public int minCost(int[][] costs) {
        int red = costs[0][0];
        int blue = costs[0][1];
        int green = costs[0][2];

        for (int i = 1; i < costs.length; i++) {
            int newRed = Math.min(blue, green) + costs[i][0];
            int newBlue = Math.min(red, green) + costs[i][1];
            int newGreen = Math.min(red, blue) + costs[i][2];

            red = newRed;
            blue = newBlue;
            green = newGreen;
        }

        return Math.min(red, Math.min(blue, green));
    }
}
