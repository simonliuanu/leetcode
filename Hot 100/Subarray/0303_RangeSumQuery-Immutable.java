// First try
class NumArray {
    int[] num;

    public NumArray(int[] nums) {
        num = nums;
    }

    public int sumRange(int left, int right) {
        int sum = 0;
        for (int i = left; i < right + 1; i++) {
            sum += num[i];
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */

class NumArray {
    int[] sums;

    public NumArray(int[] nums) {
        sums = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
    }

    public int sumRange(int left, int right) {
        return sums[right + 1] - sums[left];
    }
}
