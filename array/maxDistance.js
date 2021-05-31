var maxDistance = function (nums1, nums2) {
    distances = [0]

    for (var i = 0; i < nums1.length; i++) {
        for (var j = 0; j < nums2.length; j++) {
            if (nums1[i] <= nums2[j]) {
                distances.push(j - i)
            }
        }
    }

    return distances.sort((a, b) => b - a)[0]
};


console.log(maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]))