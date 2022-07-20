"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return None
        stack=[root]
        while stack:
            n=len(stack)
            for i in range(n-1):
                u=stack.pop(0)
                u.next=stack[0]
                if u.left!=None:
                    stack.append(u.left)
                if u.right!=None:
                    stack.append(u.right)
            u=stack.pop(0)
            u.next=None
            if u.left!=None:
                stack.append(u.left)
            if u.right!=None:
                    stack.append(u.right)
        return root
                