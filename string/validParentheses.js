// https://leetcode.com/problems/valid-parentheses/


/**
 * @param {string} s
 * @return {boolean}
 */
// Time: O(n), Space: O(n)
const isValid = function (s) {
    const par = { "{": "}", "[": "]", "(": ")" }

    let stack = []

    for (let i = 0; i < s.length; i++) {
        if (par[s[i]]) {
            stack.push(par[s[i]])
        } else if (stack.length && stack[stack.length - 1] == s[i]) {
            stack.pop()
        } else {
            return false
        }
    }

    return stack.length === 0
}