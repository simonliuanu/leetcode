import java.sql.Array;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[][] diagonalSort(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;

        List<List<Integer>> diag = new ArrayList<>(n + m);

        for (int i = 0; i < n + m; i++) {
            diag.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                diag.get(i - j + m).add(mat[i][j]);

            }
        }

        for (List<Integer> d : diag) {
            Collections.sort(d, Collections.reverseOrder());
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                mat[i][j] = diag.get(i - j + m).removeLast();
            }
        }

        return mat;
    }
}
