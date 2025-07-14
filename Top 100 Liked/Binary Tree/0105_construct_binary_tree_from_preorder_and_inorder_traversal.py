# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {val: idx for idx, val in enumerate(inorder)}
        pre = 0

        def build(l: int, r: int) -> TreeNode:
            if l > r:
                return None

            nonlocal pre
            node = TreeNode(preorder[pre])
            pre += 1

            mid = mp.get(node.val)

            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)

            return node

        return build(0, len(inorder) - 1)
