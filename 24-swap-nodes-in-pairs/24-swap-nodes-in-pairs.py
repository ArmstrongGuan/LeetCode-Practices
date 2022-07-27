# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front=ListNode()
        front.next=head
        before=front
        dummy=head
        while dummy and dummy.next:
            behind=dummy.next.next
            before.next=dummy.next
            dummy.next=dummy.next.next
            before.next.next=dummy
            before=dummy
            dummy=dummy.next
        return front.next
            