# https://leetcode.com/problems/binary-tree-level-order-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return root

        array = []

        # call travel method on root with empty array and initial level set to 0
        self.travel(root, array, 0)

        return array

    def travel(self, node: TreeNode, array: list, level: int):
        try:
            # push current node value in array[current level]
            # if array doesn't have array[level] set, it will fail and execute to except block
            array[level].append(node.val)
        except:
            # if array[level] is not set then push in array
            array.append([node.val])

        if node.left:
            # call travel method on left node with current level + 1
            self.travel(node.left, array, (level + 1))

        if node.right:
            # call travel method on right node with current level + 1
            self.travel(node.right, array, (level + 1))
