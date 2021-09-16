class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n)
# Space: O(n)


def levelOrder(root: TreeNode) -> list:
    if not root:
        return []

    result = []

    q = [root]

    while(len(q)):
        length = len(q)
        count = 0
        subArr = []

        while(count < length):
            currentNode = q.pop(0)

            subArr.append(currentNode.val)

            if currentNode.left:
                q.append(currentNode.left)

            if currentNode.right:
                q.append(currentNode.right)

            count += 1

        result.append(subArr)

    return result


rootNode = TreeNode(3,  TreeNode(6, TreeNode(9, None, TreeNode(
    5, TreeNode(8))), TreeNode(2)), TreeNode(1, None, TreeNode(4)))

print(levelOrder(rootNode))
