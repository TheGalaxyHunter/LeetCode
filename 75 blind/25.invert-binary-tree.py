# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print the tree in tree form
def print_tree(root: TreeNode, space: int = 0, is_left: bool = True):
    if root == None:
        return

    space += 5
    print_tree(root.right, space, False)
    print()
    for i in range(5, space):
        print(end=" ")
    print(root.val)
    print_tree(root.left, space, True)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root
    

sol = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
root = sol.invertTree(root)
print_tree(root)




        