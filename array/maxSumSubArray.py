class Solution:
    def num(self, s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    def checkSubarraySum(self, nums: list, k: int) -> bool:
        max_sum = nums[0]
        curr_sum = max_sum

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(curr_sum, max_sum)

        print(max_sum / k)
        print(self.num(('%f' % (max_sum / k)).rstrip('0').rstrip('.')))

        return type(self.num(('%f' % (max_sum / k)).rstrip('0').rstrip('.'))) is int


print(Solution().checkSubarraySum([23, 2, 4, 6, 6], 7))
