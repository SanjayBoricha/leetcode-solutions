const totalRainWater = function (heights) {
    let totalWater = 0

    for (let p = 0; p < heights.length; p++) {
        const ch = heights[p]

        let maxL = 0
        let maxR = 0

        let leftP = p
        while (leftP < heights.length) {
            maxL = Math.max(maxL, heights[leftP])
            leftP++
        }

        let rightP = p
        while (rightP >= 0) {
            maxR = Math.max(maxR, heights[rightP])
            rightP--
        }

        const currentWater = Math.min(maxR, maxL) - ch

        if (currentWater >= 0) {
            totalWater += currentWater
        }
    }

    return totalWater
}

console.log(totalRainWater([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]));