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

The main part is row calculation and column caluclation 
- 
"""


# Complexoty
"""
time complexity of this would be O( m * logn)  m being the arrays we have in the matrix list  
"""

# Code

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left+ right) // 2

        # convert to a 2D array 

        row = mid // n
        col = mid % n 

        mid_value = matrix[row][col]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else: 
            right = mid - 1
    
    return False 

"""
The beauty is that we get O(log(m×n)) time complexity because we're doing binary search on the 
conceptually flattened array, but we never actually create that flattened array - 
we just use math to map between the 1D search space and 2D coordinates.

"""