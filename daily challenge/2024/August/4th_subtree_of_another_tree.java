/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return dfs(root, subRoot);
    }

    public boolean dfs(TreeNode r, TreeNode s) {
        if(r == null) return false;
        return check(r, s) || dfs(r.left, s) || dfs(r.right, s);
    }

    public boolean check(TreeNode r, TreeNode s) {
        if (r == null && s == null) return true;
        if (r == null || s == null || r.val != s.val) return false;
        return check(r.left, s.left) && check(r.right, s.right);
    }
}
