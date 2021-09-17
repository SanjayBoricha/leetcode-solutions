# https://leetcode.com/problems/binary-tree-right-side-view/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideViewBFS(root: TreeNode) -> list:
    if not root:
        return []

    result = []

    q = [root]

    while(len(q)):
        length = len(q)
        count = 0

        currentNode = None

        while(count < length):
            currentNode = q.pop(0)

            if currentNode.left:
                q.append(currentNode.left)

            if currentNode.right:
                q.append(currentNode.right)

            count += 1

        result.append(currentNode.val)

    return result


def rightSideViewDFS(node: TreeNode, result={}, level=1) -> list:
    if not node:
        return []

    if not level in result.keys():
        result[level] = node.val

    if node.right:
        rightSideViewDFS(node.right, result, level + 1)

    if node.left:
        rightSideViewDFS(node.left, result, level + 1)

    return list(result.values())


rootNode = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(
    7, TreeNode(8))), TreeNode(5)), TreeNode(3, None, TreeNode(6)))

"""
            1
          /   \
        2       3
      /   \       \
    4       5       6
      \
        7
      /
    8
"""

print("BFS: ", end="")
print(rightSideViewBFS(rootNode))

print("DFS: ", end="")
print(rightSideViewDFS(rootNode))
