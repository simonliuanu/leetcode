class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }

        int l = 0;
        int r = sum;

        for (int i = 0; i < nums.length; i++) {
            if (i > 0) l += nums[i - 1];
            if (i < nums.length) r -= nums[i];

            if (l == r) return i;
        }

        return -1;
    }
}

