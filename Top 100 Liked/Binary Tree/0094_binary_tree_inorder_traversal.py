# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion solution:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        def inorder(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans

# iteration solution:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans

# Morris Traversal solution(O(1) in extra space):
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if not root.left:
                ans.append(root.val)
                root = root.right
            else:
                p = root.left
                while p.right and p.right != root:
                    p = p.right
                if not p.right:
                    p.right = root
                    root = root.left
                else:
                    # Add the following expression to restore the original structure
                    p.right = None
                    ans.append(root.val)
                    root = root.right
        return ans


