"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        result=Node(head.val)
        stack1=[head] #for the original list
        stack2=[result] #for the new list
        cur=result
        while head.next:
            cur.next=Node(head.next.val)            
            cur=cur.next
            stack2.append(cur)            
            head=head.next
            stack1.append(head)
        for i in range(len(stack1)):
            if stack1[i].random!=None:
                stack2[i].random=stack2[stack1.index(stack1[i].random)]
        return result
            