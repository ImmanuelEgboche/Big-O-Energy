class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
