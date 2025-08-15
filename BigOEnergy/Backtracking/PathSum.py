from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        remainingsum = targetSum - root.val
        left_result = self.hasPathSum(root.left, remainingsum)
        right_result = self.hasPathSum(root.right, remainingsum)
        
        return left_result or right_result


root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

Solution.hasPathSum()