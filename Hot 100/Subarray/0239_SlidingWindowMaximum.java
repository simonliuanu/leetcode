// First try, out of time:
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];
        int l = 0, r = k - 1;
        for (int i = 0; i < nums.length - k + 1; i++) {
            int max = Integer.MIN_VALUE;
            for (int j = l; j <= r; j++) {
                max = Math.max(max, nums[j]);
            }
            ans[i] = max;
            l++;
            r++;
        }
        return ans;
    }
}
