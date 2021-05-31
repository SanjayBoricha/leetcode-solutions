class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def gotoLast(self, node: TreeNode, depth: int) -> list:
        arr = []

        if(node == None):
            return [1]

        if(node.left):
            leftArr = self.gotoLast(node.left, depth + 1)
            arr.extend(leftArr)

        if(node.right):
            rightArr = self.gotoLast(node.right, depth + 1)
            arr.extend(rightArr)

        if(node.left == None and node.right == None):
            arr.append(depth)

        return arr

    def isBalanced(self, root: TreeNode) -> bool:
        arr = self.gotoLast(root, 1)
        arr.sort()

        print(arr)

        return (arr[len(arr) - 1] - arr[0] < 2)


# root = TreeNode(1, TreeNode(2, TreeNode(
#     3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))

# root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))

print(Solution().isBalanced(root))
