# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list:
        if not root:
            return root

        array = []

        self.travel(root, array, 0)

        return array

    def travel(self, node: Node, array: list, lvl: int):
        try:
            array[lvl].append(node.val)
        except:
            array.append([node.val])

        if node.children:
            for child in node.children:
                self.travel(child, array, (lvl + 1))


tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

print(Solution().levelOrder(tree))
