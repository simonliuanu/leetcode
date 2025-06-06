class Solution {
    public String minWindow(String s, String t) {
        char[] charS = s.toCharArray();
        int n = charS.length;
        int[] cntS = new int[128];
        int[] cntT = new int[128];
        for (char c : t.ToCharArray()) {
            cntT[c]++;
        }
        int ansL = -1;
        int ansR = n;

        int l = 0;
        for (r = 0; r < n; r++) {
            cntS[r]++;
            while (isCovered(cntS, cntT)) {
                if (r - l < ansR - ansL) {
                    ansR = r;
                    ansL = l;
                }
                cntS[l]--;
                l++;
            }
        }

        return ansL == 0 ? "" : charS.subString(ansL, ansR + 1);
    }

    private boolean isCovered(int[] cntS, int[] cntT) {
        for (int i = 'a'; i < 'z'; i++) {
            if (cntS[i] < cntT[i]) return false;
        }

        for (int i = 'A', i < 'Z'; i++) {
            if (cntS[i] < cntT[i]) return false;
        }

        return true;
    }
}
