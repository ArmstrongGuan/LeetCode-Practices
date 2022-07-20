# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isthesame(root, subRoot):
            if subRoot==None:
                return True if root == None else False
            if root==None:
                return False
            if root.val!=subRoot.val:
                return False
            return (isthesame(root.left, subRoot.left) and isthesame(root.right, subRoot.right))
        queue=[root]
        while queue:
            u=queue.pop(0)
            if isthesame(u, subRoot):
                return True
            if u.left!=None:
                queue.append(u.left)
            if u.right!=None:
                queue.append(u.right)
        return False