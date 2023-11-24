from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_pointer = 0
        s_pointer = 0
        result = 0
        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                g_pointer += 1
                s_pointer += 1
                result += 1
            else:
                s_pointer += 1
        return result

print(Solution().findContentChildren([1, 2, 3], [1,1]))
print(Solution().findContentChildren([1, 2], [1, 2, 3]))
print(Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))