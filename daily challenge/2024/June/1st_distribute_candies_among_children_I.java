// Brute-force solution
class Solution {
    public int distributeCandies(int n, int limit) {
        int ret = 0;
        for (int i = 0; i <= limit; i++) {
            for (int j = 0; j <= limit; j++) {
                if (i + j > n) break;
                if (n - i - j <= limit) ret++;
            }
        }
        return ret;
    }
}
