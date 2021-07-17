# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return root

        array = []

        self.travel(root, array)

        return array

    def travel(self, node: TreeNode, array: list):
        array.append(node.val)

        if node.left:
            self.travel(node.left, array)

        if node.right:
            self.travel(node.right, array)


tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))

print(Solution().inorderTraversal(tree))
