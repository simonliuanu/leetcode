// Own solution, brute-force, O(mn)
class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        int[] answer = new int[2];
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    answer[0]++;
                    break;
                }
            }
        }

        for (int i = 0; i < nums2.length; i++) {
            for (int j = 0; j < nums1.length; j++) {
                if (nums2[i] == nums1[j]) {
                    answer[1]++;
                    break;
                }
            }
        }
        return answer;
    }
}

// Hashing solution, O(m + n), however this solution is slower than the previous one in test, maybe because of the test data
class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> set2 = new HashSet<>();
        int[] ans = new int[2];
        for (int i : nums1) {
            set1.add(i);
        }
        for (int i : nums2) {
            set2.add(i);
        }
        for (int i : nums1) {
            if (set2.contains(i)) ans[0]++;
        }
        for (int i : nums2) {
            if (set1.contains(i)) ans[1]++;
        }
        return ans;
    }
}
