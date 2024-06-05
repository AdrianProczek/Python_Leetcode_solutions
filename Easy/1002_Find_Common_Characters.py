# 1002. Find Common Characters
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

 

# Constraints:

#     1 <= words.length <= 100
#     1 <= words[i].length <= 100
#     words[i] consists of lowercase English letters.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common_words = Counter(words[0])
        for word in words[1:]:
            common_words &= Counter(word)

        output = []
        for char, count in common_words.items():
            output.extend([char] * count)

        return output