/**
 * https://leetcode.com/problems/add-two-numbers/
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function addTwoNumbers(l1, l2) {
    let n1 = l1
    let n2 = l2

    let firstSumNode = null
    let sumNode = null

    let carry = 0

    while (n1 || n2) {
        let v1 = n1 ? n1.val : 0
        let v2 = n2 ? n2.val : 0

        let sum = v1 + v2 + carry
        carry = Math.floor(sum / 10)

        if (sumNode) {
            sumNode.next = new ListNode(sum % 10)
            sumNode = sumNode.next
        } else {
            sumNode = new ListNode(sum % 10)
            firstSumNode = sumNode
        }

        n1 = n1 ? n1.next : null
        n2 = n2 ? n2.next : null
    }

    if (carry) {
        sumNode.next = new ListNode(carry)
        sumNode = sumNode.next
    }

    return firstSumNode
}

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
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

let list1 = createList([9, 9, 9, 9, 9, 9, 9])
let list2 = createList([9, 9, 9, 9])

function getValues(node) {
    let arr = []

    let tempNode = node
    while (tempNode) {
        arr.push(tempNode.val)
        tempNode = tempNode.next
    }

    return arr
}

console.log(JSON.stringify(getValues(addTwoNumbers(list1, list2))))
