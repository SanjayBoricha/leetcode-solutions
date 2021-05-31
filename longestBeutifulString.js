var longestBeautifulSubstring = function (word) {
    var vowels = ['a', 'e', 'i', 'o', 'u']

    var subStr = ''
    var found = false

    for (var i = 0; i < word.length; i++) {
        if (found) break

        if (!subStr && word[i] === 'a') {
            subStr += word[i]
        } else if (subStr[subStr.length - 1] !== undefined && (vowels.indexOf(word[i]) == vowels.indexOf(subStr[subStr.length - 1]) + 1 || vowels.indexOf(word[i]) == vowels.indexOf(subStr[subStr.length - 1]))) {
            subStr += word[i]

            if (vowels.indexOf(subStr[subStr.length - 1]) === vowels.length - 1 && word[i + 1] !== 'u') {
                found = true
            }
        } else {
            subStr = ''
        }
    }

    return subStr.length >= 5 ? subStr.length : 0
};


console.log(longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))