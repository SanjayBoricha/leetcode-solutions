var removeDuplicates = function (nums) {
    nums = nums.filter((num, i) => {
        return num !== nums[i + 1]
    })

    return nums
};

let arr = [1, 1, 2]

console.log(removeDuplicates(arr))
