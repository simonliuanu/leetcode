// Own Solution O(n^3)
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int n = grid.length;
        int ret = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int maxi = grid[i][j];
                int maxj = grid[i][j];
                for (int m = 0; m < n; m++) {
                    maxi = Math.max(maxi, grid[i][m]);
                }
                for (int m = 0; m < n; m++) {
                    maxj = Math.max(maxj, grid[m][j]);
                }
                ret += Math.min(maxi, maxj) - grid[i][j];
            }
        }
        return ret;
    }
}

// Official Solution O(n^2)
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int n = grid.length;
        int[] rowMax = new int[n];
        int[] colMax = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rowMax[i] = Math.max(rowMax[i], grid[i][j]);
                colMax[j] = Math.max(colMax[j], grid[i][j]);
            }
        }
        int ret = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ret += Math.min(rowMax[i], colMax[j]) - grid[i][j];
            }
        }
        return ret;
    }
}
