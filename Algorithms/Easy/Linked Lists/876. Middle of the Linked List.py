# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_array = []
        double_head = head
        while head:
            result_array.append(head.val)
            head = head.next
        key_elem = len(result_array) // 2
        while key_elem > 0:
            double_head = double_head.next
            key_elem -= 1
        return double_head

