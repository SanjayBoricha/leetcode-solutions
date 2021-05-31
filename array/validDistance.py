class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        d = 0

        for i in range(len(nums1)):
            for j in range(i, len(nums2)):
                if(i <= j and nums1[i] <= nums2[j] and (j - i) > d):
                    d = (j - i)

        return d
