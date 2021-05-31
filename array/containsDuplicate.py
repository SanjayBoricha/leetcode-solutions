# https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()

        for i in range(len(nums)):
            if(nums[i] in hash_set):
                return True

            hash_set.add(nums[i])

        return False


print(Solution().containsDuplicate([1, 2, 4, 6, 3, 2]))
