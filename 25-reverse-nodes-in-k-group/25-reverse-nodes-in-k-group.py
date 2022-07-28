# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front=ListNode()
        front.next=head
        before=front
        dummy=head
        stack=[]
        while dummy:
            stack.append(dummy)
            dummy=dummy.next
            if len(stack)==k:
                #print(before, dummy, stack)
                for i in range(k-1,0,-1):
                    stack[i].next=stack[i-1]
                before.next=stack[-1]
                before=stack[0]
                before.next=dummy
                stack=[]
        return front.next