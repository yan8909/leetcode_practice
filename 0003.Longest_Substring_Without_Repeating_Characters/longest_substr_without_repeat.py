# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        start = 0 # 左端點
        seen = {}

        for i in range(n):
            if s[i] not in seen: # i:右端點
                maxLength = max(maxLength, i - start + 1)
            else:
                # case 1 : s[i]於左右端點間，將左端點移至s[i]+1
                if seen[s[i]] >= start:
                    start = seen[s[i]] + 1
                # case 2 : s[i]於端點外，繼續移動
                else:
                    maxLength = max(maxLength, i - start + 1)
            seen[s[i]] = i
        return maxLength 

test = Solution()
s = "abcabcbb"
print(test.lengthOfLongestSubstring(s))