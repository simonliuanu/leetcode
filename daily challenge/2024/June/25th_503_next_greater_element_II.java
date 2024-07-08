// own solution, brute-force, extremely slow
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n];
        for (int i = 0; i < n; i++) {
            int current = nums[i];
            ret[i] = Integer.MIN_VALUE;
            for (int j = 0; j < n; j++) {
                if (nums[(i + j) % n] > current) {
                    ret[i] = nums[(i + j) % n];
                    break;
                }
            }
            if (ret[i] == Integer.MIN_VALUE) ret[i] = -1;
        }
        return ret;
    }
}

