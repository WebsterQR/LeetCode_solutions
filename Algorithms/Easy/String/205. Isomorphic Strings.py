class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letters_1 = set(s)
        letters_2 = set(t)
        pairs = set([(s[i], t[i]) for i in range(len(s))])
        if len(pairs) == len(letters_1) == len(letters_2):
            return True
        return False

print(Solution().isIsomorphic('egg', 'add'))
print(Solution().isIsomorphic('foo', 'bar'))
print(Solution().isIsomorphic('paper', 'title'))