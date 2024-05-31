// Brute-force solution
class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int[] cnt = new int[n * n + 1];
        int[] ret = new int[2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cnt[grid[i][j]] ++;
            }
        }

        for (int i = 1; i < n * n + 1; i++) {
            if (cnt[i] == 0) ret[1] = i;
            if (cnt[i] == 2) ret[0] = i;
        }

        return ret;
    }
}
