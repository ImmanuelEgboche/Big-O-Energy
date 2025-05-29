"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.

Return the number of unique elements (k), such that the first k elements of nums contain the final result.

⚠️ Rules:

You must not use extra space (no new arrays).

The final result should be in the first k slots of nums.

After k, we don’t care what’s in the array.

"""

# we go through the list and check against a condition that looks to see the unique occurance is happening more than twice 

# it replaces those postions where its happening more than twice so nothing actaully being removed just postiton being swapped then anything after the point we need or our second pointer K we ignore boom

nums = [1,1,1,2,2,3]

k = 0

for i in range(len(nums)):
    if k < 2 or nums[i] != nums[k-2]:
        nums[k] = nums[i]
        k+=1
    
nums[:k]