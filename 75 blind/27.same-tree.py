# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val == q.val:
            return (True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else:
            return False
        

sol = Solution()
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(sol.isSameTree(p, q), "\tActual: True")

p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
print(sol.isSameTree(p, q), "\tActual: False")

p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print(sol.isSameTree(p, q), "\tActual: False")

p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(2), TreeNode(1))
print(sol.isSameTree(p, q), "\tActual: True")

p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print(sol.isSameTree(p, q), "\tActual: False")