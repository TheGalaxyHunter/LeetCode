# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(-float("infinity"), root, float("infinity"))

    def valid(self, lb, root, rb):
        if not root:
            return True
        
        if lb < root.val < rb:
            return (self.valid(lb, root.left, root.val) and self.valid(root.val, root.right, rb))

        else:
            return False


sol = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(sol.isValidBST(root), "\tExpected: True")

root = TreeNode(5, TreeNode(1), TreeNode(9, TreeNode(6), TreeNode(10)))
print(sol.isValidBST(root), "\tExpected: True")

root = TreeNode(1, TreeNode(1))
print(sol.isValidBST(root), "\tExpected: False")