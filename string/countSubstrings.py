# https://leetcode.com/problems/palindromic-substrings/

# Time: O(n^2), Space: O(1)
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         counter = 0

#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 subStr = s[i:j + 1]

#                 if(subStr and subStr == subStr[::-1]):
#                     counter += 1

#         return counter

class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                subStr = s[i:j + 1]

                if(subStr and subStr == subStr[::-1]):
                    counter += 1

        return counter


print(Solution().countSubstrings("aaa"))
