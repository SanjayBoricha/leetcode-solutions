# https://leetcode.com/problems/backspace-string-compare/submissions/

# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         typedS = self.typeString(s)
#         typedT = self.typeString(t)

#         return typedS == typedT

#     def typeString(self, s: str):
#         typed = []

#         for c in s:
#             if(c == "#"):
#                 if(len(typed)):
#                     typed.pop()
#             else:
#                 typed.append(c)

#         return typed

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1

        while(p1 >= 0 or p2 >= 0):
            if(s[p1] == '#' or t[p2] == '#'):
                if(s[p1] == '#'):
                    backCount = 2
                    while(backCount > 0):
                        p1 -= 1
                        backCount -= 1
                        if(s[p1] == '#'):
                            backCount = backCount + 2

                if(t[p2] == '#'):
                    backCount = 2
                    while(backCount > 0):
                        p2 -= 1
                        backCount -= 1
                        if(t[p2] == '#'):
                            backCount = backCount + 2

            else:
                if(s[p1] != t[p2]):
                    return False
                else:
                    p1 -= 1
                    p2 -= 1

        return True


print(Solution().backspaceCompare("aa#b", "adc##b"))
