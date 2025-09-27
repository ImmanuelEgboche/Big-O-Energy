import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) # turns nums into a in-heap
        while len(self.heap) > k: # shrink to size k
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) # adding a new number
        if len(self.heap) > self.k: # pop the smallest fo too heavy
            heapq.heappop(self.heap)
        return self.heap[0] # kth largest is smallest in heap 