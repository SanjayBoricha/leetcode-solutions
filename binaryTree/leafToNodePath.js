/**
 * https://leetcode.com/problems/binary-tree-paths/
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}


function binaryTreePaths(root) {
    let paths = [];

    getPath(root, [], paths)

    return paths
}

function getPath(node, path, paths) {
    path = [...path, node.val]

    if (!node.left && !node.right) {
        paths.push(path)
    }

    if (node.left) getPath(node.left, path, paths)
    if (node.right) getPath(node.right, path, paths)
}

// function arrayToBinaryTree(arr) {
//     let rootNode = new TreeNode(arr[0])
//     let treeNode = rootNode

//     arr.shift()
//     arr.forEach(n => {
//         if (treeNode.left || n === null) {
//             treeNode.right = new TreeNode(n)
//             treeNode = treeNode.right
//         } else {
//             treeNode.left = new TreeNode(n)
//         }
//     })

//     return rootNode
// }

let node = new TreeNode(1)

node.left = new TreeNode(2)
node.left.right = new TreeNode(5)

node.right = new TreeNode(3)

console.log(binaryTreePaths(node))
