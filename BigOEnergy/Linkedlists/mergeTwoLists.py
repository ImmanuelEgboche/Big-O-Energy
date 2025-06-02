"""
Uses two pointer technique but has two sorted lists which is a clue 

So we need to walk through both lists

one for list 1 and one for list 2 

At each point we compare and take teh smaller node. At each point we take the best immediate option

This wasy each node is visted once O(n) and no new nodes O(1) space

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # could traverse one upload to linked list then at each node check if teh other linked list node val is equal to or less than the one im looking at then slap it in
        # or could traverse both linked lists at the same time then add the smaller one into the new list first if equal too add both 
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
    
    