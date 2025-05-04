// Brute-Force solution, probably time out oc.
class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int cnt = 0;
        for (int i = 0; i < dominoes.length; i++) {
            for (int j = i + 1; j < dominoes.length; j++) {
                if ((dominoes[i][0] == dominoes[j][0] && dominoes[i][1] == dominoes[j][1]) || (dominoes[i][0] == dominoes[j][1] && dominoes[i][1] == dominoes[j][0]))
                cnt++;
            }
        }
        return cnt;
    }
}

// Direct-address table
class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int cnt = 0;
        int arr[] = new int[100];
        for (int[] domino : dominoes) {
            int val = domino[0] < domino[1]
                    ? domino[0] * 10 + domino[1]
                    : domino[1] * 10 + domino[0];
            cnt += arr[val];
            arr[val]++;
        }
        return cnt;
    }
}
