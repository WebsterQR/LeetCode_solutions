from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        num = 0
        while num < len(nums):
            result += min(nums[num], nums[num+1])
            num += 2
        return result