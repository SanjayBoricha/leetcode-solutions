class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    # Time: O(n), Space: O(1)
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        current = head

        while current:
            if(current.child):
                next_node = current.next

                child = current.child
                current.child = None

                current.next = child
                child.prev = current

                end_of_child = child

                while(end_of_child.next):
                    end_of_child = end_of_child.next

                end_of_child.next = next_node
                if next_node:
                    next_node.prev = end_of_child

            current = current.next

        return head


def createDoublyLinkedList(arr):
    head = Node(arr[0])
    current_node = head

    for i in range(1, len(arr)):
        val = arr[i]
        next_node = None

        if(type(val) is list):
            next_node = createDoublyLinkedList(val)
            current_node.child = next_node
        else:
            next_node = Node(val)
            current_node.next = next_node
            next_node.prev = current_node
            current_node = next_node

    return head


def createArray(head: Node):
    arr = []

    current = head
    while current:
        arr.append(current.val)

        if(current.child):
            arr.append(createArray(current.child))

        current = current.next

    return arr


arr = [1, [2, 7, [8, 10, 11], 9], 3, 4, [5, 12, 13], 6]
doubly_head = createDoublyLinkedList(arr)


print('arr', createArray(doubly_head))

print(createArray(Solution().flatten(doubly_head)))
