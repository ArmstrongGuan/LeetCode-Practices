# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead=ListNode(-101)
        newhead.next=head
        cur=newhead
        while cur.next and cur.next.next:
            if cur.next.val==cur.next.next.val:
                pointer=cur.next.next.next
                value=cur.next.val
                while pointer and pointer.val==value:
                    pointer=pointer.next
                cur.next=pointer
            else:
                cur=cur.next
        return newhead.next
            