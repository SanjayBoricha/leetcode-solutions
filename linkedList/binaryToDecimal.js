/**
 * https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 */

var getDecimalValue = function (head) {
    let arr = []

    let tempNode = head
    while (tempNode) {
        arr.push(tempNode.val)
        tempNode = tempNode.next
    }

    return parseInt(arr.join(''), 2)
};
