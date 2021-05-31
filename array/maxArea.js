// https://leetcode.com/problems/container-with-most-water/

var maxArea = function (height) {
    var max = 0
    var distance = 1

    for (var i = 0; i < height.length; i++) {
        for (var j = 0; (j < height.length) && j !== i; j++) {
            var newMax = height[i] > height[j] ? (height[j] * height[j]) : (height[i] * height[i])
            var newDistance = j > i ? j - i : i - j

            if ((newMax > max) || newDistance > distance) {
                distance = newDistance
                max = newMax > distance ? newMax : distance
            }
        }
    }

    return max
};

let arr = [1, 2, 4, 3]

console.log(maxArea(arr))