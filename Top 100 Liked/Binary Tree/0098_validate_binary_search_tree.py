# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Preorder solution:
class Solution:
    def isValidBST(self, root: Optional[TreeNode], l=-inf, r=inf) -> bool:
        if not root:
            return True
        v = root.val
        return l < v < r and self.isValidBST(root.left, l, v) and self.isValidBST(root.right, v, r)

# Inorder solution:
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
