"""
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.
"""

from typing import Optional, List

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def __repr__(self):
        ""'Helper method to print the linked list'""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

 
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists using a min-heap.

    The key insight: We only need to compare the first element at any gien time since the linked
    lists are sorted
    """

    # Creat a min heap to store (value, unique_id, node) tuples
    # We need unique_id because ListNode objects aren't directly comparable 

    heap = []

    #Steo 1 Put the head node of each linked list into the heap
    for i, head in enumerate(lists):
        if head: #Only adds non-empty lists
            # Push (value, unique_identifer, node) to avoid comparison issues
            heapq.heappush(heap, (head.val, i, head))

    #Create a dummy head for easier list construction
    dummy = ListNode(0)
    current = dummy

    #Counter for unique ID's
    unique_id = len(lists)

    # Step 2 - 4: Process until heap is empty
    while heap:
        #Pop the smallest node from the heap
        val, _, node = heapq.heappop(heap)

        #Add that node to merged list
        current.next = node
        current = current.next

        # if that node has a .next, push that .next into the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, unique_id, node.next))
            unique_id += 1
    return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Convert a Python list to a linked list"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage and testing
if __name__ == "__main__":
    # Create test data: 3 sorted linked lists
    list1 = create_linked_list([1, 4, 5])      # 1 -> 4 -> 5
    list2 = create_linked_list([1, 3, 4])      # 1 -> 3 -> 4  
    list3 = create_linked_list([2, 6])         # 2 -> 6
    
    print("Input lists:")
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"List 3: {list3}")
    
    # Test both implementations
    lists_copy1 = [list1, list2, list3]
    result1 = mergeKLists(lists_copy1)
    print(f"\nMerged result (v1): {result1}")
    
    # Recreate lists for second test (since we modified them)
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    lists_copy2 = [list1, list2, list3]
    result2 = mergeKLists(lists_copy2)
    print(f"Merged result (v2): {result2}")
    
    # Test edge cases
    print("\nEdge cases:")
    print("Empty lists:", mergeKLists([]))
    print("Single list:", mergeKLists([create_linked_list([1, 2, 3])]))
    print("Lists with None:", mergeKLists([None, create_linked_list([1]), None]))






