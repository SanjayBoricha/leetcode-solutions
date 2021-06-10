import requests


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> list:
        prev = None
        current = head

        while current:
            n = current.next
            current.next = prev
            prev = current
            current = n

        a = []
        s = []
        current = prev

        while current:
            x = current.val
            while s and s[-1] <= x:
                s.pop()

            if s:
                a.append(s[-1])
            else:
                a.append(0)
                s.append(x)
                current = current.next

        return a[::-1]


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


url = 'https://leetcode-testcases.netlify.app/504699948/data.json'

response = requests.get(url)

array = response.json()

print(Solution().nextLargerNodes(arrayToLinkedList(array)))

# print(response.json())
