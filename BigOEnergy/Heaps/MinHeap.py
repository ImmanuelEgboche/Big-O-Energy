class Heap:
    def __init__(self):
        # Start with a dummy element at index 0 to make 1 indexed math work 
        self.heap = [0]

    def push(self,val):
        """Insert new element - O(log n)"""
        #Add to end to maintain complete tree property
        self.heap.append(val)
        i = len(self.heap) - 1

        # Bubble up (percolate up) to maintain heap property
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            # Swap with parent if current is smaller
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    
    def pop(self):
        """Remove and return minimum element - O(log n)"""
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop() #Only 1 element
        
        # STore min value to return
        result = self.heap[1]

        # Move last element to root (maintains complete tree)
        self.heap[1] = self.heap.pop()

        #Bubble down (percolate down) to restore heap property
        i = 1
        while 2 * i < len(self.heap): # While has left child 
            # Determine which child to potentially swap with
            min_child = 2 * i + 1 # right child is smaller

            # check if right child exists and is smaller than left
            if (2 * i + 1 < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[2 * i]):
                min_child = 2 * i + 1 # Right child is smaler

            # If curremt node is larger than smallest child, swap
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break
        return result
    def peek(self):
        """Get minimum without removing - O(1)"""
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        """Build heap from array - O(n)"""
        # Move first element to end for 1 indexed approach
        arr.append(arr[0])
        self.heap = arr

        # Start from last non leaf node and bubble down
        # lAST NON LEAF IS AT (n-1)//2 in 1 indexed array
        start = (len(self.heap)-1) // 2

        for i in range(start, 0, -1):
            self._bubble_down(i)

    def _bubble_down(self, i):
        """Helper function for bubble down operation"""
        while 2 * i < len(self.heap):
            min_child = 2 * i # left child

            # Check if right child exisits and is smaller
            if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i]):
                min_child = 2 * i + 1

            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break