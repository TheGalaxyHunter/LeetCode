# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameSubtree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



    def sameSubtree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True

        elif t1 and t2 and t1.val == t2.val:
            return (self.sameSubtree(t1.left, t2.left) and self.sameSubtree(t1.right, t2.right))

        return False
    
sol = Solution()
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(sol.isSubtree(root, subRoot), "\tExpected: True")

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(sol.isSubtree(root, subRoot), "\tExpected: False")

root = TreeNode(1, TreeNode(1))
subRoot = TreeNode(1)
print(sol.isSubtree(root, subRoot), "\tExpected: True")