# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        ans = float('inf')
        sum1 = 0
        j = 0

        for i in range(len(nums)):
            sum1 += nums[i]

            while sum1 >= target:
                ans = min(ans, i-j+1)
                sum1 -= nums[j]
                j += 1

        return ans if ans < float('inf') else 0


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
