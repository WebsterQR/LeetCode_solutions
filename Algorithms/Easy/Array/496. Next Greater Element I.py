from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for el in nums1:
            found = False
            position = nums2.index(el)
            for i in range(position + 1, len(nums2)):
                if nums2[i] > el:
                    result.append(nums2[i])
                    found = True
                    break
            if not found:
                result.append(-1)
        return result


assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
assert Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
print('Tests passed!')