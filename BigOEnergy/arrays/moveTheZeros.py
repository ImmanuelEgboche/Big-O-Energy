"""
You are given an integer array nums. Move all zeroes to the end of the array while maintaining the relative order of the non-zero elements.
You must do this in-place without making a copy of the array.

Return the array is not required—you just modify nums in-place.

Input: nums = [0,1,0,3,12]
Output: nums = [1,3,12,0,0]


"""

# if no array we just return default value or if no zeros just return the array 

# to move something to the end we need to know where the end is

# secondly we need to knwo where the zeros are we can easily do that with a for loop

# in terms of repostitoning these we find a value of zero lets say its at num[1] we then assign it to num[len(nums)-1]

# if we keep finding more we do the same?

def movethezeros(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k+=1
    
    for j in range(k, len(nums)):
        nums[j] = 0


