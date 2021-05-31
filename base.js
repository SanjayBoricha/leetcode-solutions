var sumBase = function (n, k) {
    var nums = parseInt(n, 10).toString(k).split('');
    var sum = 0;

    nums.forEach(num => {
        sum += parseInt(num)
    })

    return sum
};

console.log(sumBase(34, 6))