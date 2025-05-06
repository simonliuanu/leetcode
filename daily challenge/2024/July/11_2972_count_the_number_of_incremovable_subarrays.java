class Solution {
    public long incremovableSubarrayCount(int[] nums) {
        int n = nums.length;
        int l = 0;
        long ret = 0;
        while (l < n - 1) {
            if (nums[l] >= nums[l + 1]) break;
            l++;
        }
        if (l == n - 1) return (long) (n * (n + 1)) / 2;
        else ret += l + 2;

        for (int r = n - 1; r > 0; r--) {
            if (r < n - 1 && nums[r] >= nums[r + 1]) break;
            while (l >= 0 && nums[l] >= nums[r]) l--;
            ret += l + 2;
        }

        return ret;
    }
}
