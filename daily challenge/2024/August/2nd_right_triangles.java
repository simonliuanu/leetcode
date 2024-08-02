class Solution {
    public long numberOfRightTriangles(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[] sumCol = new int[n];
        int[] sumRow = new int[m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sumCol[i] += grid[i][j];
                sumRow[j] += grid[i][j];
            }
        }
        long ret = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ret += grid[i][j] * (sumCol[i] - 1) * (sumRow[j] - 1);
            }
        }
        return ret;
    }
}
