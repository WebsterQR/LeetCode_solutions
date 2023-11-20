class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(set(pattern)) != len(set(words)) or len(pattern) != len(words):
            return False
        mapping = {el: '' for el in pattern}
        for num, el in enumerate(pattern):
            if mapping[el] == '':
                mapping[el] = words[num]
            else:
                if mapping[el] == words[num]:
                    continue
                else:
                    return False
        return True


print(Solution().wordPattern('abba', 'dog cat cat dog'))
print(Solution().wordPattern('abba', 'dog cat cat fish'))
print(Solution().wordPattern('aaaa', 'dog cat cat dog'))