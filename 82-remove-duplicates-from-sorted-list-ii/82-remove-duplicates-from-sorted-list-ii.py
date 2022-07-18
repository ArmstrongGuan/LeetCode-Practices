# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        stack=[]
        cur=-101
        appeared=False
        while dummy:
            #print(stack)
            if cur==dummy.val:
                if appeared==False:
                    appeared=True
                    stack.pop()
                    dummy=dummy.next
                else:
                    dummy=dummy.next
            else:
                stack.append(dummy)
                cur=dummy.val
                appeared=False
                dummy=dummy.next
        if len(stack)==0:
            return None
        for i in range(len(stack)-1):
            stack[i].next=stack[i+1]
        stack[-1].next=None
        head=stack[0]
        return head