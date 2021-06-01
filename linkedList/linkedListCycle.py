# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        fast = head.next
        slow = head

        while(fast != None and fast.next != None and slow != None):
            if(fast == slow):
                return True

            fast = fast.next.next
            slow = slow.next

        return False


head = ListNode(2, ListNode(4, ListNode(7, ListNode(5))))

head.next.next.next = head.next

print(Solution().hasCycle(head))
