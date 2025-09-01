"""
You are given the root of a binary tree. Return only the values of 
the nodes that are visible from the right side of the tree, ordered from top to bottom.

"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root:
            queue.append(root)
        arr = []
        while len(queue) > 0:
            level_size = len(queue)
            for i in range(level_size): # how are we traversing each level adn checking sides?
                curr = queue.popleft

                if i == level_size - 1:  # i assume this is what is gettin the most right side node
                    arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return arr
