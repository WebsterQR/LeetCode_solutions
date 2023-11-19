class Solution:
    def correct_pair(self, branch_open: str, branch_close: str) -> bool:
        if branch_open == '(' and branch_close == ')':
            return True
        if branch_open == '{' and branch_close == '}':
            return True
        if branch_open == '[' and branch_close == ']':
            return True
        return False

    def isValid(self, s: str) -> bool:
        opened_order = list()
        last_opened_number = -1
        for el in s:
            if el in ['(', '{', '[']:
                if last_opened_number == len(opened_order) - 1:
                    opened_order.append(el)
                    last_opened_number += 1
                else:
                    opened_order[last_opened_number + 1] = el
                    last_opened_number += 1
            else:
                if last_opened_number == -1:
                    return False
                if not self.correct_pair(opened_order[last_opened_number], el):
                    return False
                last_opened_number -= 1
        if last_opened_number == -1:
            return True
        return False