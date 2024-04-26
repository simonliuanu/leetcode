import java.util.LinkedList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */

// Using recursion
class Solution {
    public List<Integer> list;

    public List<Integer> preorderTraversal(TreeNode root) {
        list = new LinkedList<>();

        if (root == null)
            return list;

        preorderRecur(root);

        return list;
    }

    public void preorderRecur(TreeNode node) {
        if (node == null)
            return;

        list.add(node.val);

        preorderRecur(node.left);
        preorderRecur(node.right);
    }
}

// Using iteration
class Solution {
    public List<Integer> list;

    public List<Integer> preorderTraversal(TreeNode root) {
        list = new LinkedList<>();

        if (root == null)
            return list;

        Stack<TreeNode> stack = new Stack<>();

        stack.push(root);

        while (!stack.isEmpty()) {
            TreeNode current = stack.pop();
            list.add(current.val);
            if (current.right != null)
                stack.push(current.right);
            if (current.left != null)
                stack.push(current.left);
        }

        return list;
    }
}
