# https://leetcode.com/problems/backspace-string-compare/submissions/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        typedS = self.typeString(s)
        typedT = self.typeString(t)

        return typedS == typedT

    def typeString(self, s: str):
        typed = []

        for c in s:
            if(c == "#"):
                if(len(typed)):
                    typed.pop()
            else:
                typed.append(c)

        return typed


print(Solution().backspaceCompare("a#b", "dc##b"))
