class Solution {
    public int findChampion(int[][] grid) {
        for (int i = 0; i < grid.length; i++) {
            int sum = 0;
            for (int j : grid[i]) {
                sum += j;
            }
            if (sum == grid.length - 1)
                return i;
        }
        return -1;
    }
}
