# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        self.res = defaultdict(list)
        self.levelTraverse(root, 0)
        return self.res.values()

    def levelTraverse(self, root: TreeNode, lvl: int):
        if root:
            self.res[lvl].append(root.val)

            self.levelTraverse(root.left, lvl+1)
            self.levelTraverse(root.right, lvl+1)


sol = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(list(sol.levelOrder(root)))

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(list(sol.levelOrder(root)))

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(list(sol.levelOrder(root)))

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
print(list(sol.levelOrder(root)))
