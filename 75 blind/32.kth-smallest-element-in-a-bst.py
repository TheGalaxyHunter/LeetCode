# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # return self.traverse(root)[k-1]
        self.res = []
        self.k = k
        self.traverse_update(root)
        return self.res[k-1]

    def traverse(self, root):
        if not root:
            return []
        return self.traverse(root.left) + [root.val] + self.traverse(root.right)

    def traverse_update(self, root):
        if not root:
            return

        if len(self.res) >= self.k:
            return

        self.traverse_update(root.left)
        self.res.append(root.val)
        self.traverse_update(root.right)
    

sol = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(sol.kthSmallest(root, 1), "Actual: 1")
print(sol.kthSmallest(root, 2), "Actual: 2")
print(sol.kthSmallest(root, 3), "Actual: 3")
print(sol.kthSmallest(root, 4), "Actual: 4")
