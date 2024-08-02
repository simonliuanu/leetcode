// Solution using stack
class Solution {
    public int calPoints(String[] operations) {
        int n = operations.length, top = 0;
        int[] stack = new int[n];
        int ret = 0;
        for (int i = 0; i < n; i++) {
            String str = operations[i];
            if (str.equals("+")) {
                stack[top] = stack[top - 1] + stack[top - 2];
                ret += stack[top];
            } else if (str.equals("D")) {
                stack[top] = 2 * stack[top - 1];
                ret += stack[top];
            } else if (str.equals("C")) {
                ret -= stack[top - 1];
                top -= 2;
            } else {
                stack[top] = Integer.parseInt(str);
                ret += stack[top];
            }
            top++;
        }
        return ret;
    }
}
