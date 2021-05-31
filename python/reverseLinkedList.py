class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        node = head
        prev = None

        while (node != None):
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        return prev


head = ListNode(1)
prev = head

i = 2
while(i <= 5):
    prev.next = ListNode(i)
    prev = prev.next
    i += 1


def linkedListToArray(node: ListNode) -> list:
    current = node
    arr = []

    while(current != None):
        arr.append(current.val)
        current = current.next

    return arr


print('Input', end=" : ")
print(linkedListToArray(head))

print('Result', end=" : ")
print(linkedListToArray(Solution().reverseList(head)))
