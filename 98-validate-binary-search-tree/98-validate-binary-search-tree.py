# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(root, low, high):
            if root == None:
                return True
            if root.val< high and root.val>low:
                return (checkBST(root.left, low, root.val) and checkBST(root.right, root.val, high))
            else:
                return False
        return checkBST(root, -2**31-1, 2**31)
        