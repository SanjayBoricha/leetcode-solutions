class Solution:
    def splitString(self, s: str) -> bool:
        arr = []
        lastEnd = 0
        for i in range(1, len(s)):
            if(int(s[i - 1]) > int(s[i]) and int(s[i]) != 0):
                arr.append(int(s[lastEnd:i]))
                lastEnd = i

        if(lastEnd < len(s)):
            arr.append(int(s[lastEnd:len(s)]))

        print(arr)
        for i in range(len(arr) - 1):
            if(arr[i] < arr[i + 1]):
                return False

        return True


print(Solution().splitString('1234'))
print(Solution().splitString('050043'))
print(Solution().splitString('9080701'))
print(Solution().splitString('10009998'))
print(Solution().splitString('3202872336'))
