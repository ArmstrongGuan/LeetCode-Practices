# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        harshmap={}
        while cur:
            if cur in harshmap:
                return cur
            else:
                harshmap[cur]=True
                cur=cur.next
        return cur
            