class Solution {
    public int findValueOfPartition(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int gap = Integer.MAX_VALUE;
        for (int i = 0; i < n - 1; i++) {
            if ((nums[i + 1] - nums[i]) < gap) {
                gap = nums[i + 1] - nums[i];
            }
        }
        return gap;
    }
}
