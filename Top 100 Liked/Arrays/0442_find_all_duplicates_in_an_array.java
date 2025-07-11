// hashset solution:
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        Set<Integer> hashset = new HashSet<>();
        int n = nums.length;
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!hashset.contains(nums[i])) {
                hashset.add(nums[i]);
            } else {
                ans.add(nums[i]);
            }
        }
        return ans;
    }
}

// in-place hashing solution:
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int n = nums.length;
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            while (nums[i] != nums[nums[i] - 1]) {
                swap(nums, i, nums[i] - 1);
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                ans.add(nums[i]);
            }
        }
        return ans;
    }

    private void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}
