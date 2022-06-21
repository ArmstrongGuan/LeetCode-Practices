# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def orderwithlevel(root, level, result):
            if root != None:
                if len(result) < level+1:
                    result+=[[]]
                result[level]= result[level]+[root.val]
                result = orderwithlevel(root.left, level+1, result)
                result = orderwithlevel(root.right, level+1, result)
            else:
                return result
            return result
        return orderwithlevel(root, 0, [])
            