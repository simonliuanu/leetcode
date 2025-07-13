# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        self.ans = None

        def inorder(node: Optional[TreeNode]):
            nonlocal cnt
            if not node or self.ans is not None:
                return
            inorder(node.left)
            cnt += 1
            if cnt == k:
                self.ans = node.val
            inorder(node.right)

        inorder(root)
        return self.ans
