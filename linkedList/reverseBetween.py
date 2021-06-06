# https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time: O(n), Space: O(1)
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        current_pos = 1
        current_node = head
        start = head

        while(current_pos < left):
            start = current_node
            current_node = current_node.next
            current_pos += 1

        new_list = None
        tail = current_node

        while(current_pos >= left and current_pos <= right):
            next_node = current_node.next
            current_node.next = new_list
            new_list = current_node
            current_node = next_node
            current_pos += 1

        start.next = new_list
        tail.next = current_node

        if(left > 1):
            return head

        return new_list


def linkedListToArray(head):
    arr = []
    node = head

    while(node != None):
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
