class Solution {
    public int maxOperations(int[] nums) {
        if (nums.length < 2) return 0;

        int sum = nums[0] + nums[1];
        int cnt = 1;
        for (int i = 2; i < nums.length; i+=2) {
            if (nums.length < i + 2) return cnt;
            if (nums[i] + nums[i + 1] == sum) cnt++;
            else return cnt;
        }
        return cnt;
    }
}
