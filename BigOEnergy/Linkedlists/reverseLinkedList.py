"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Would need a prev to check the element we've passed to be able to make that the next

class Solution:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            while curr:
                 next_node = curr.next
                 curr.next = prev 

                 prev = curr
                 curr = next_node
            
            return prev
            
