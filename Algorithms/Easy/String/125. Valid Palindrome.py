class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ''.join([el.lower() for el in list(s) if el.isalpha() or el.isdigit()])
        return True if str1 == str1[::-1] else False