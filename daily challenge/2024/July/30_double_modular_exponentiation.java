class Solution {
    public List<Integer> getGoodIndices(int[][] variables, int target) {
        List<Integer> ret = new ArrayList<>();
        for (int i  = 0; i < variables.length; i++) {
            int[] v = variables[i];
            if (powMod(powMod(v[0], v[1], 10), v[2], v[3]) == target) {
                ret.add(i);
            }
        }
        return ret;
    }

    public int powMod(int x, int y, int mod) {
        int ret = 1;
        while (y != 0) {
            if ((y & 1) == 1) {
                ret = ret * x % mod;
            }
            x = x * x % mod;
            y >>= 1;
        }
        return ret;
    }
}
