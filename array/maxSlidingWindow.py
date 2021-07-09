import requests
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        l = deque([])
        for i in range(k):
            while l and nums[i] >= nums[l[-1]]:
                l.pop()
            l.append(i)
        ans = [nums[l[0]]]

        for i in range(1, len(nums)-k+1):
            while(l and nums[i+k-1] >= nums[l[-1]]):
                l.pop()
            l.append(i+k-1)
            if i-1 == l[0]:
                l.popleft()
            ans.append(nums[l[0]])
        return ans


url = 'https://leetcode-testcases.netlify.app/518525103/data.json'

response = requests.get(url)

array = response.json()

print(Solution().maxSlidingWindow(array, 1000))
