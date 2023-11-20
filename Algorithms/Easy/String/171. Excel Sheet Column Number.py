class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = 0
        columnTitle = columnTitle[::-1]
        grade = 0
        for symbol in columnTitle:
            result = result + (alph.index(symbol) + 1) * 26**grade
            grade += 1
        return result


print(Solution().titleToNumber('A'))
print(Solution().titleToNumber('AB'))
print(Solution().titleToNumber('FXSHRXW'))
