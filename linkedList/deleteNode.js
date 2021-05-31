// https://leetcode.com/problems/delete-node-in-a-linked-list/

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function deleteNode(node) {
    console.log(node)
}

let nodeToDelete = null

function createList(arr, d) {
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

        if (v === d) {
            nodeToDelete = node
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

console.log(getValues(createList([1, 2, 3, 4], 3)))

deleteNode(nodeToDelete)
