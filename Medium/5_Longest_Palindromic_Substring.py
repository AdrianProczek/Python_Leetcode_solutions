# 5. Longest Palindromic Substring
# Given a string s, return the longest
# palindromic
# substring
# in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_pal = ""
        for i in range(len(s)):
            p = ""
            for n in range(i, len(s)):
                p += s[n]
                if p == p[::-1]:
                    pal = p
            if len(l_pal) < len(pal):
                l_pal = pal
        return l_pal