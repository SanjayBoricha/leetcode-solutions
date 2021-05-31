var maxFrequency = function (nums, k) {
    var op = k
    var index = 0;

    nums.sort((a, b) => a - b)

    while (op) {
        // if (nums.findIndex(n => n === nums[index]) === -1) {
        nums[index] += 1
        // }
        console.log(nums)
        if (nums.findIndex(n => n === nums[index]) !== -1) {
            index++
        }
        op--
    }

    return nums
};

console.log(maxFrequency([1, 2, 4], 5))
