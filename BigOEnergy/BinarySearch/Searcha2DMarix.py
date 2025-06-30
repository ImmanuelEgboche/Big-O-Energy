"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""

# Intuition
"""
Im thinkinig we for loop through the amrtix and for each array we run binary search
but to get it in log(m*n) we're gonn have to multipy the 2d array some how

OR 

The matrix is sorted like a single increasig lists if we add each row together so if we have the m *n elements
we could do binary search on a 1d array instead
"""

# Approach
"""
simple approach we for loop through and run binary seatch 

OR 

Treat the matrix as a virtual sorted array of length m*n as its a 2d array
Use binary search with left as 0 and teh right as m*n -1 that would now be the last point
- 
"""


# Complexoty
"""
time complexity of this would be O( m * logn)  m being the arrays we have in the matrix list  
"""

# Code