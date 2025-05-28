"""
You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

Note:

The order of the unique elements should remain the same as in the original array.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain all the unique elements.
Return k as the final result.

"""
# If the  nums is empty just return 0 - nothing to do

# Set pointer that looks for where the enxt unique elements should
# start at the start

#if the current element is different from the previous one:
# new unique
# move the pointer forward

#return the pointer as the number of unique elements

class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        #Handles empty list 
        if not nums:
            return 0
        
        # Start the pointer at index 1 (since nums[0] is always unique)
        k = 1

        # Loop through nums starting from index 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i] # Place the unique element at position
                k+=1 # Move pointer to the next spot 
        
        return k