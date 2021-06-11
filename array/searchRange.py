# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

import math


class Solution:
    # Time: O(log n), Space: O(1)
    def searchRange(self, nums: list, target: int) -> list:
        left = self.searchLeftIndex(nums, target)
        right = self.searchRightIndex(nums, target)

        return [left, right]

    def searchLeftIndex(self, nums, target):
        index = -1

        start = 0
        end = len(nums) - 1

        while(start <= end):
            mid = math.floor(start + (end - start) / 2)

            if(nums[mid] >= target):
                end = mid - 1
            else:
                start = mid + 1

            if(nums[mid] == target):
                index = mid

        return index

    def searchRightIndex(self, nums, target):
        index = -1

        start = 0
        end = len(nums) - 1

        while(start <= end):
            mid = math.floor(start + (end - start) / 2)

            if(nums[mid] <= target):
                start = mid + 1
            else:
                end = mid - 1

            if(nums[mid] == target):
                index = mid

        return index


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
