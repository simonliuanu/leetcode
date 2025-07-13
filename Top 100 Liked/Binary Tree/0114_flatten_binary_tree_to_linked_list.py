# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion solution:
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

# iteration solution:
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        s = [root]
        p = None

        while s:
            c = s.pop()
            if p:
                p.left = None
                p.right = c
            if c.right:
                s.append(c.right)
            if c.left:
                s.append(c.left)
            p = c

# O(1) in space, predecessor solution:
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        while root:
            if root.left:
                p = nxt = root.left
                while p.right:
                    p = p.right
                p.right = root.right
                root.left = None
                root.right = nxt
            root = root.right
