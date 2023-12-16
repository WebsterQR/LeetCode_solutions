class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict = dict()
        for jewel in jewels:
            jewels_dict[jewel] = 1
        result = 0
        for stone in stones:
            if jewels_dict.get(stone):
                result += 1
        return result
