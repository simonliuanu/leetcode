// Backtracing
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        List<Integer> path = new ArrayList<>();
        boolean[] used = new boolean[n];

        List<List<Integer>> ans = new ArrayList<>();

        backtrack(nums, n, path, used, ans);

        return ans;
    }

    private void backtrack(int[] nums, int n, List<Integer> path, boolean[] used, List<List<Integer>> ans) {
        if (path.size() == n) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (used[i]) continue;

            path.add(nums[i]);
            used[i] = true;

            backtrack(nums, n, path, used, ans);

            used[i] = false;

            path.remove(path.size() - 1);
        }
    }
}
