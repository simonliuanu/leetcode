// Recursion method
class Solution {
    List<Integer> list = new ArrayList<>();

    public List<Integer> inorderTraversal(TreeNode root) {
        inorder(root);
        return list;
    }

    public void inorder(TreeNode node) {
        if (node == null)
            return;

        inorder(node.left);
        list.add(node.val);
        inorder(node.right);
    }
}

// Iteration method
