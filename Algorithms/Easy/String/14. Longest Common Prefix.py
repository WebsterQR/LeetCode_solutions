from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        base = strs[0]
        for letter in base:
            longest_prefix += letter
            if all([word.startswith(longest_prefix) for word in strs]):
                continue
            return longest_prefix[:-1]
        return base