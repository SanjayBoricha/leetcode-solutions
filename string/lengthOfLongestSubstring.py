# https://leetcode.com/problems/longest-substring-without-repeating-characters

# time: O(n^2), space: O(n)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0

#         for i in range(len(s)):
#             hash_map = set()
#             for j in range(i, len(s)):
#                 if not s[j] in hash_map:
#                     hash_map.add(s[j])
#                     longest = max(longest, len(hash_map))
#                 else:
#                     break

#         return longest


# time: O(n), space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        left = 0
        right = 0

        has_map = set()

        while(left < len(s) and right < len(s)):
            if not s[right] in has_map:
                has_map.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                has_map.remove(s[left])
                left += 1
                longest = max(longest, right - left)

        return longest


print(Solution().lengthOfLongestSubstring("abcabcbb"))
