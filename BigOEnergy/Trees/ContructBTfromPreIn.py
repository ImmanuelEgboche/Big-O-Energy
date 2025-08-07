"""
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]


"""


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val

        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Map from value to its index in order for O(1) look ups
        index_map = {val: i for i, val in enumerate(inorder)}

        #Pointer to current root in preorder
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            #Pick the current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            #Build the root node
            root = TreeNode(root_val)

            #Index of the root in inorder
            index = index_map[root_val]

            #Recursively build left and right subtree
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root
                