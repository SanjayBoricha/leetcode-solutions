function maxArea(height) {
    let a = 0, b = height.length - 1

    let largest = 0

    while (a < b) {
        largest = Math.max(largest, Math.min(height[a], height[b]) * (b - a))

        if (height[a] <= height[b]) {
            a++
        } else {
            b--
        }
    }

    return largest
};

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))