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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        stack=[root]
        root.next=None
        while stack[-1].left:
            count=len(stack)+1
            for i in range((count-2)//2,count-1):                    
                stack.append(stack[i].left)
                stack.append(stack[i].right)
            for i in range(count-1,2*count-1):
                print("i = ", i)
                if i==2*count-2:
                    stack[i].next= None
                else:
                    stack[i].next=stack[i+1]
        return root
            
            