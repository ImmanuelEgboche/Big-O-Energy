"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # O(n) time complexity as we travel to each node
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def helper(node):
            if not node:
                return

            helper(node.left)
            arr.append(node.val)
            helper(node.right)

        helper(root)

        return arr[k-1]

class Solution1: # O(h) being teh height of the tree
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None 

        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)

            self.count +=1 
            if self.count == k:
                self.result = node.val
                return

            inorder(node.right)
        inorder(root)

        return self.result
    

