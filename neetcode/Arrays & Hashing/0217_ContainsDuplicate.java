// Own solution O(n^2), exceeds time
class Solution {
    public boolean containsDuplicate(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (nums[i] == nums[j] && i != j) return true;
            }
        }
        return false;
    }
}

// Official solution I: Sorting
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
}

// Official solution II: HashSet
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int x: nums) {
            if (!set.add(x)) {
                return true;
            }
        }
        return false;
    }
}
