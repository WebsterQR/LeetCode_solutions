class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for num, el in enumerate(s):
            if num > 0 and mapping[s[num - 1]] < mapping[s[num]]:
                result += (mapping[el] - 2 * mapping[s[num-1]])
            else:
                result += mapping[el]
        return result