class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
    

sol = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.maxDepth(root))

root = TreeNode(1, None, TreeNode(2))
print(sol.maxDepth(root))

root = None
print(sol.maxDepth(root))