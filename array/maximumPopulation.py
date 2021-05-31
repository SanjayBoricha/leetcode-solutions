# https://leetcode.com/problems/maximum-population-year

class Solution:
    def maximumPopulation(self, logs: list) -> int:
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))

        dates.sort()

        print(dates)

        population = 0
        max_population = 0
        max_year = 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year

        return max_year


print(Solution().maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]))
