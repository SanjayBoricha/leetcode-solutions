// https://leetcode.com/problems/reverse-linked-list/

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function reverseList(head) {
    let reversed = createList(getValues(head).reverse())

    return reversed
}

function createList(arr) {
    let firstNode = null
    let node = null

    arr.forEach((v) => {
        if (!node) {
            node = new ListNode(v)
            firstNode = node
        } else {
            node.next = new ListNode(v)
            node = node.next
        }
    })

    return firstNode
}

function getValues(node) {
    let arr = []

    let tempNode = node
    while (tempNode) {
        arr.push(tempNode.val)
        tempNode = tempNode.next
    }

    return arr
}

console.log(getValues(reverseList(createList([1, 2, 3, 4, 5]))))