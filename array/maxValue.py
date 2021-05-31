class Solution:
    def maxValue(self, n: str, x: int) -> str:
        maxVal = None
        start = int(n) < 0 if 1 else 1

        for i in range(start, len(n) + 1):
            temp = n[:i] + str(x) + n[i:]

            if(maxVal == None):
                maxVal = int(temp)
            else:
                maxVal = max(maxVal, int(temp))

        return maxVal


print(Solution().maxValue("-13", 2))
