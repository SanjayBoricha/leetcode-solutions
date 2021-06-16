# https://leetcode.com/problems/remove-linked-list-elements/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time: O(n), Space: O(1)
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        while(head and head.val == val):
            head = head.next

        current = head
        prev = None

        while current:
            if(current.val == val):
                prev.next = current.next
                current = prev

            prev = current
            current = current.next

        return head


def createLinkedList(arr: list):
    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


def linkedListToArray(node: ListNode):
    arr = []

    while node:
        arr.append(node.val)
        node = node.next

    return arr


head = createLinkedList([1, 2, 6, 3, 4, 5, 6])

print(linkedListToArray(Solution().removeElements(head, 6)))

head = createLinkedList([7, 7, 7, 7])

print(linkedListToArray(Solution().removeElements(head, 7)))
