// hashset solution
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


