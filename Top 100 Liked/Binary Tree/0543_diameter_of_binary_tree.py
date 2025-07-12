# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion:
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal ans
            ans = max(ans, l + r)
            return max(l, r) + 1

        dfs(root)
        return ans
