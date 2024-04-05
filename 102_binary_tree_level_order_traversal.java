import java.util.ArrayList;
import java.util.Queue;

import javax.swing.tree.TreeNode;

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

// Solution using recursion
class Solution {
    List<List<Integer>> levels = new ArrayList<>();

    public void helper(TreeNode node, int level) {
        if (levels.size() == level) {
            levels.add(new ArrayList<>());
        }

        levels.get(level).add(node.val);

        if (node.left != null) {
            helper(node.left, level + 1);
        }
        if (node.right != null) {
            helper(node.right, level + 1);
        }

    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null)
            return levels;

        helper(root, 0);

        return levels;
    }
}

// Solution using Queue
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        if (root != null) {
            queue.offer(root);
        }

        while(!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> list = new ArrayList<>();
            while(size-- > 0) {
                TreeNode node = queue.peek();
                queue.pool();
                list.add(node.val);

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            ret.add(list);
        }
        return ret;
    }
}
