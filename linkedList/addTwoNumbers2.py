import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode) -> object:
        current = head
        prev = None
        length = 0

        while(current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            length += 1

        return prev

    # Time: O(n), Space: O(n)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r1 = self.reverse(l1)
        r2 = self.reverse(l2)

        carry = 0

        prev = ListNode(0)
        head = prev

        while(r1 or r2 or carry):
            v1 = r1.val if r1 else 0
            v2 = r2.val if r2 else 0

            current_sum = v1 + v2 + carry
            carry = math.floor(current_sum / 10)
            node = ListNode(current_sum % 10)
            prev.next = node
            prev = node

            if r1:
                r1 = r1.next

            if r2:
                r2 = r2.next

        return self.reverse(head.next)


def linkedListToArray(head):
    arr = []
    node = head

    while(node != None):
        arr.append(node.val)
        node = node.next

    return arr


l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))

print(linkedListToArray(Solution().addTwoNumbers(l1, l2)))
