class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> combine = new ArrayList<Integer>();
        dfs(candidates, target, ret, combine, 0);
        return ret;
    }

    public void dfs(int[] candidates, int target, List<List<Integer>> ret, List<Integer> combine, int index) {
        if (index == candidates.length) {
            return;
        }
        if (target == 0) {
            ret.add(new ArrayList<Integer>(combine));
            return;
        }

        dfs(candidates, target, ret, combine, index + 1);

        if (target - candidates[index] >= 0) {
            combine.add(candidates[index]);
            dfs(candidates, target - candidates[index], ret, combine, index);
            combine.remove(combine.size() - 1);
        }
    }
}
