# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: list) -> int:
        totalWater = 0

        p1 = 0
        p2 = len(height) - 1

        maxR = 0
        maxL = 0

        while(p1 < p2):
            if(height[p1] <= height[p2]):
                if(maxL > height[p1]):
                    totalWater += (maxL - height[p1])
                else:
                    maxL = height[p1]

                p1 += 1
            else:
                if(maxR > height[p2]):
                    totalWater += (maxR - height[p2])
                else:
                    maxR = height[p2]

                p2 -= 1

        return totalWater


print(Solution().trap([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))
