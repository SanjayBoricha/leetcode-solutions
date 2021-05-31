// https://leetcode.com/problems/merge-strings-alternately/

var mergeAlternately = function (s1, s2) {
    var maxLength = s1.length > s2.length ? s1.length : s2.length

    var merged = '';

    for (var i = 0; i < maxLength; i++) {
        if (i < s1.length) {
            merged += s1[i]
        }

        if (i < s2.length) {
            merged += s2[i]
        }
    }

    return merged
};


console.log(mergeAlternately("abcd", "pq"))