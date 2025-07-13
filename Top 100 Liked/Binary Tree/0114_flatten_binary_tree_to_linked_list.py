# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        for i in range(len(ans) - 1):
            ans[i].left = None
            ans[i].right = ans[i + 1]
