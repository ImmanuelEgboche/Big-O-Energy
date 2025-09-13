"""
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
"""

from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, target, path):
            if target == 0:
                res.append(path[:])
                return
            if target < 0 or i == len(nums):
                return
            
            path.append(nums[i])
            backtrack(i, target - nums[i], path)
            path.pop()