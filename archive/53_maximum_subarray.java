// Brute Force solution, won't pass all tests
class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum > max)
                    max = sum;
            }
        }
        return max;
    }
}

// Dynamic Programming solution
class Solution {
    public int maxSubArray(int[] nums) {
        int dp = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > 0)
                nums[i] += nums[i - 1];
            if (dp < nums[i])
                dp = nums[i];
        }
        return dp;
    }
}
