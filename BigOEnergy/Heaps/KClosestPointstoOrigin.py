"""
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.
"""

def kClosest(points, k):
    #Calculate sqaured distances
    distances = [(x*x + y*y, [x,y]) for x,y in points]

    # Sort by distance
    distances.sort(key=lambda p: p[0])

    # take the first k pointers
    return [point for _, point in distances[:k]]
"""
Instead of sorting all n points (O(n log n)), we keep a heap of size k

Pythons heapq is a min heap by default 

but we want to keep the k closest which means we want to throw out the farthest when the heap gets 
too big

To do that we can store negative distances so the largets distance acts like the smallest in the heap
"""

import heapq

def kHeapCloest(points, k):
    heap = []

    for x, y in points:
        dist = x*x + y*y
        # push negative distance to simulate max-heap
        heapq.heappush(heap, (-dist, x,y))

        if len(heap) > k:
            heapq.heappop(heap) # remove farthest point
    
    return [[x,y] for (_, x, y) in heap]
