# https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        node = head
        leftNode = None
        prevNode = head

        while (node):
            if(node.val == left):
                leftNode = prevNode

            if(node.val == right):
                next_node = leftNode.next
                leftNode.next = node
                node.next = next_node

            prevNode = node
            node = node.next

        return head


def linkedListToArray(head):
    arr = []
    node = head

    while(node):
        arr.append(node.val)
        node = node.next

    return arr


def arrayToLinkedList(arr):
    head = None
    prevNode = None

    for i in range(len(arr)):
        newNode = ListNode(arr[i])

        if(not head):
            head = newNode
        else:
            prevNode.next = newNode

        prevNode = newNode

    return head


head = arrayToLinkedList([1, 2, 3, 4, 5])
left = 2
right = 4

print(linkedListToArray(Solution().reverseBetween(head, left, right)))
