import requests


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def createStackFromLinkedList(self, node: ListNode) -> list:
        stack = []

        while node:
            stack.append(node.val)
            node = node.next

        return stack

    def nextLargerNodes(self, head: ListNode) -> list:
        stack = self.createStackFromLinkedList(head)

        nextLargests = []

        for i in range(len(stack)):
            found = False
            for j in range(i, len(stack)):
                if(stack[j] > stack[i]):
                    nextLargests.append(stack[j])
                    found = True
                    break

            if not found:
                nextLargests.append(0)

        return nextLargests


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
