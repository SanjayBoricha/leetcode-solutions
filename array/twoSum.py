# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         p1 = 0
#         p2 = 1

#         while(p1 < len(nums)):
#             if(nums[p1] + nums[p2] == target):
#                 return [p1, p2]
#             elif(p2 == len(nums) - 1):
#                 p1 += 1
#                 p2 = p1 + 1
#             else:
#                 p2 += 1

#         return []

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        ntf = {}

        for i in range(len(nums)):
            ntf[target - nums[i]] = i

        for i in range(len(nums)):
            try:
                index = ntf[nums[i]]
            except:
                index = False

            if(index != False):
                return [i, index]


print(Solution().twoSum([1, 3, 7, 9, 2], 11))
