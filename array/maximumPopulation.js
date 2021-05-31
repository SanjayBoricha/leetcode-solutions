var maximumPopulation = function (logs) {
    populationByYears = {}

    for (var i = 1; i < logs.length; i++) {
        if (logs[i][0] - 1 <= logs[i - 1][1]) {
            if (populationByYears[logs[i - 1][1] - 1]) {
                console.log('x')
                populationByYears[logs[i - 1][1] - 1] += 1
            } else {
                populationByYears[logs[i - 1][1] - 1] = 1
            }
        }
    }

    console.log(populationByYears)

    return 0
};

console.log(maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]))