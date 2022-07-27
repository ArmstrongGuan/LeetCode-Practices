# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack=[]
        dummy=head
        while dummy:
            stack.append(dummy)
            dummy=dummy.next
        n=len(stack)
        if n<2:
            return head
        k=- k%n
        stack[-1].next=stack[0]
        stack[k-1].next=None
        return stack[k]
        