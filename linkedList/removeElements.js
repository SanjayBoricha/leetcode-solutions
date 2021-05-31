var removeElements = function (head, val) {
    let node = head

    while (node.val === val) {
        node = node.next
    }

    return node
};


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

console.log(removeElements(createList([7, 7, 7, 7, 6]), 7))