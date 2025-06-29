//Backtracing
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();

        backtrack(nums, 0, new ArrayList<>(), ans);

        return ans;
    }

    private void backtrack(int[] nums, int idx, List<Integer> path, List<List<Integer>> ans) {
        if (idx == nums.length) {
            ans.add(new ArrayList<>(path));
            return;
        }

        backtrack(nums, idx + 1, path, ans);

        path.add(nums[idx]);
        backtrack(nums, idx + 1, path, ans);
        path.remove(path.size() - 1);
    }
}
