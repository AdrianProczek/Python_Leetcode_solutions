# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

#     1 <= s.length <= 3 * 105
#     s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [x for x in s if x.lower() in ("a", "e", "i", "o","u")]
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i].lower() in ("a", "e", "i", "o","u"):
                s_list[i] = vowels.pop()
        return "".join(s_list)