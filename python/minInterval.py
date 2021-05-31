class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        pq = []
        k = 0
        ans = [-1] * len(queries)
        for query, i in sorted(zip(queries, range(len(queries)))):
            while k < len(intervals) and intervals[k][0] <= query:
                heappush(pq, (intervals[k][1] -
                         intervals[k][0] + 1, *intervals[k]))
                k += 1
            while pq and pq[0][2] < query:
                heappop(pq)
            if pq:
                ans[i] = pq[0][0]
        return ans


print(Solution().minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))

# nums = [3, 5, 4, 63, 3]
# print(nums.index(3))
