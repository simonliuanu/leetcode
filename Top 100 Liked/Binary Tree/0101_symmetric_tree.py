# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion:
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
            if not l and not r:
                return True
            elif not l or not r:
                return False
            else:
                return l.val == r.val and check(l.left, r.right) and check(l.right, r.left)

        return check(root.left, root.right)

# Iteration:
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if not l and not r:
                continue
            elif not l or not r or l.val != r.val:
                return False
            q.append((l.left, r.right))
            q.append((l.right, r.left))
        return True
