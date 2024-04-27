class Solution {
    public int[]  findColumnWidth(int[][] grid) {
        int[] ret = new int[grid[0].length];
        for (int j = 0; j < grid[0].length; j++) {
            int max = 0;
            for (int i = 0; i < grid.length; i++) {
                int temp = 0;
                if (grid[i][j] < 0) temp++;
                if (grid[i][j] == 0) temp++;
                while(grid[i][j] != 0) {
                    grid[i][j] /= 10;
                    temp++;
                }
                if (max < temp) max = temp;
            }
            ret[j] = max;
        }
        return ret;
    }
}
