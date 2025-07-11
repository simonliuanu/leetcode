//Backtracing
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();

        backtrack(candidates, ans, new ArrayList<>(), 0, target);

        return ans;
    }

    void backtrack(int[] candidates, List<List<Integer>> ans, List<Integer> path, int idx, int remain) {
        if (remain == 0) {
            ans.add(new ArrayList<>(path));
            return;
        } else if (remain < 0) return;

        for (int i = idx; i < candidates.length; i++) {
            int pick = candidates[i];

            path.add(pick);
            backtrack(candidates, ans, path, i, remain - pick);
            path.remove(path.size() - 1);
        }
    }
}
