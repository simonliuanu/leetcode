//Greedy
class Solution {
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));
        int ret = 0;
        int bnd = -1;
        for (int[] arr : points) {
            if (arr[0] > bnd) {
                bnd = arr[0] + w;
                ret++;
            }
        }
        return ret;
    }
}
