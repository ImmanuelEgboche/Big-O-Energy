from Typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val

        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int])