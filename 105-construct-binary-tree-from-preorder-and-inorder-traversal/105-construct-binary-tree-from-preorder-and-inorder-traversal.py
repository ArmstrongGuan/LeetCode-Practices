# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  
        def build(preorder, inorder):
            if len(preorder)==0:
                return None
            result= TreeNode(preorder[0])
            if len(preorder)==1:
                return result
            i=inorder.index(preorder[0])
            result.right=build(preorder[i+1:], inorder[i+1:])
            result.left=build(preorder[1:i+1], inorder[:i])
            return result
        return  build(preorder, inorder)