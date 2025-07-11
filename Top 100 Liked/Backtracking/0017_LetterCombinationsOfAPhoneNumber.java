class Solution {
    private static final String[] arr = {
        "",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.isEmpty()) {
            return new ArrayList<>();
        }

        List<String> ans = new ArrayList<>();

        backtrack(digits, 0, new StringBuilder(), ans);

        return ans;
    }

    private void backtrack(String digits, int idx, StringBuilder sb, List<String> ans) {
        if (idx == digits.length()) {
            ans.add(sb.toString());
            return;
        }

        String str = arr[digits.charAt(idx) - '0'];

        for (char c : str.toCharArray()) {
            sb.append(c);
            backtrack(digits, idx + 1, sb, ans);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
