class Solution {
    public int trap(int[] height) {
        int ret = 0;
        int l = 0, r = height.length - 1;
        int lMax = 0, rMax = 0;
        while (l < r) {
            lMax = Math.max(height[l], lMax);
            rMax = Math.max(height[r], rMax);
            if (height[l] < height[r]) {
                ret += lMax - height[l];
                l++;
            } else {
                ret += rMax - height[r];
                r--;
            }
        }
        return ret;
    }
}
