// First try:
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        int sLen = s.length();
        int pLen = p.length();
        if (sLen < pLen) return ans;
        int[] pCnt = new int[26];
        int[] wCnt = new int[26];
        for (int i = 0; i < pLen; i++) {
            pCnt[p.charAt(i) - 'a'] ++;
            wCnt[s.charAt(i) - 'a'] ++;
        }
        if (Arrays.equals(pCnt, wCnt)) ans.add(0);
        for (int i = 1; i + pLen <= sLen; i++) {
            wCnt[s.charAt(i - 1) - 'a'] --;
            wCnt[s.charAt(i + pLen - 1) - 'a'] ++;
            if (Arrays.equals(pCnt, wCnt)) ans.add(i);
        }
        return ans;
    }
}
