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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
    

sol = Solution()
print_tree(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))
print_tree(sol.buildTree([-1], [-1]))
print_tree(sol.buildTree([-1,0,1], [1,0,-1]))
print_tree(sol.buildTree([1,2,3], [3,2,1]))
print_tree(sol.buildTree([1,2,3], [1,2,3]))
