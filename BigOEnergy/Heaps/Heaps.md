# Heaps / Queues


## Key Concept
is a tree based data structre that satisfies the heap property. Its the underlying implementation for priority queues 

You can have two types heap 
- min has the smallest value at the root
- Max has teh biggest value at the root

Complete Binary Tree: All levels are filled except possibly the last, which fills left to right

Heap property: Parent-child relationship maintains order (min or max)

Array Representation: Can be efficently stored in an array without pointers 

## Complexity 

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Find Min/Max (Peek) | O(1) | O(1) | Root always contains min/max |
| Insert | O(log n) | O(1) | Bubble up to maintain heap property |
| Extract Min/Max | O(log n) | O(1) | Remove root, bubble down |
| Build from array (Heapify) | O(n) | O(1) | Surprisingly linear! |
| Increase/Decrease Key | O(log n) | O(1) | Update then bubble up/down |
| Delete arbitrary element | O(log n) | O(1) | Replace with last, then bubble |
| Merge two heaps | O(n + m) | O(n + m) | No efficient merge operation |

**Why build is O(n)**: When building a heap from a array, most of the elements are near the bottom and need minimal bubbling and mathmatucical analysis shows its linear

## Implementation insight

## Common patterns / places you want to use them

## Questions