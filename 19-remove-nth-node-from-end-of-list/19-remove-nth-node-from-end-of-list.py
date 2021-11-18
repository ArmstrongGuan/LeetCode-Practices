# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=head
        i=1
        while dummy.next!= None:
            i=i+1
            dummy=dummy.next
        dummy2=head
        if i==n:
            return head.next
        print(i)
        while i!=n+1:
            dummy2=dummy2.next
            i-=1
        dummy2.next=dummy2.next.next
        return head