# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        t = root

        if p.val <= t.val <= q.val or q.val <= t.val <= p.val:
            return t

        elif t.val < p.val and t.val < q.val:
            return self.lowestCommonAncestor(t.right, p, q)
        else:
            return self.lowestCommonAncestor(t.left, p, q)
        

sol = Solution()
root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
p = TreeNode(2)
q = TreeNode(8)
print(sol.lowestCommonAncestor(root, p, q).val, "\tActual: 6")

root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
p = TreeNode(2)
q = TreeNode(4)
print(sol.lowestCommonAncestor(root, p, q).val, "\tActual: 2")

root = TreeNode(2, TreeNode(1), TreeNode(3))
p = TreeNode(1)
q = TreeNode(3)
print(sol.lowestCommonAncestor(root, p, q).val, "\tActual: 2")