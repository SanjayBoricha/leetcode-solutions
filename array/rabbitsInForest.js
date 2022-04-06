/**
 * LeetCode Question Link: https://leetcode.com/problems/rabbits-in-forest
 *
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function(answers) {
    let map = {};
    
    let count = 0
    
    answers.forEach(ans => {
        if(map[ans]) {
            map[ans] = map[ans] - 1
        }
        
        if(!map[ans]) {
            count += (ans + 1)

            map[ans] = ans + 1
        }
    }) 
    
    return count
};
