// Solution 1 by myself, out of time when test case is large.
// I think it works correctly though.
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int len = 0;

        for (int l = 0; l < n; l++) {
            int r = l;

            while (r < n) {
                int sum = 0;
                for (int i = l; i <= r; i++) {
                    sum += nums[i];
                }
                if (sum >= target) {
                    if (len != 0) {
                        len = Math.min(len, r - l + 1);
                    } else {
                        len = r - l + 1;
                    }
                }
                r++;
            }
        }
        return len;
    }
}

// Official brute force solution
// Neater than mine, but still exceeds the time limit.
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return 0;
        }
        int ret = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                if (sum >= target) {
                    ret = Math.min(ret, j - i + 1);
                    break;
                }
            }
        }
        return ret == Integer.MAX_VALUE ? 0 : ret;
    }
}

// Sliding window solution (finally!)
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int ret = Integer.MAX_VALUE;
        int sum = 0;
        int l = 0;
        int r = 0;

        while (r < n) {
            sum += nums[r];
            while (sum >= target) {
                ret = Math.min(ret, r - l + 1);
                sum -= nums[l];
                l++;
            }
            r++;
        }
        return ret == Integer.MAX_VALUE ? 0 : ret;
    }
}
