import math


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1.sort()

        m = math.floor(len(nums1) / 2)
        if(len(nums1) / 2 > m):
            return nums1[m]
        else:
            return (nums1[m - 1] + nums1[m]) / 2


nums1 = [1, 3]
nums2 = [2]

print('ans: ', Solution().findMedianSortedArrays(nums1, nums2))
