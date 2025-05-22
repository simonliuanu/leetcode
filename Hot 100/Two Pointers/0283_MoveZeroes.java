class Solution {
    public void moveZeroes(int[] nums) {
        int l = 0, r = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[r] != 0) {
                int tmp = nums[l];
                nums[l] = nums[r];
                nums[r] = tmp;
                l++;
            }
            r++;
        }
    }
}
