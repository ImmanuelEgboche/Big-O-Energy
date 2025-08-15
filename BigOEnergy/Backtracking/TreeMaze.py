class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
If there is a solution, it will either be in the left-subtree or the right-subtree.

We can arbitrarily choose to explore the left-subtree first.
If the left-subtree returns true, we can return true as well.
If the left-subtree returns false, we can explore the right-subtree.
If the right-subtree returns true, we can return true as well.
If both the left and right subtrees return false, we can return false as well.
"""

def canReachLeaf(root):
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False

def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False

"""
The time complexity of these is O(n) as in worst case we'd have to visit every node

Space complexity is O(h) h being the heoght as we are recursively working through the max height of the tree
"""