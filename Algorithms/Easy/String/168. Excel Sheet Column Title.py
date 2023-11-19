class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        positions = list()
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while columnNumber > 0:
            columnNumber -= 1
            positions.append(alph[columnNumber % 26])
            columnNumber //= 26
        return ''.join(positions)[::-1]
