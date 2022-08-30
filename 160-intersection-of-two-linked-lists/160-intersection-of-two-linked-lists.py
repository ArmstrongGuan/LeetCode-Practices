# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        harshmap={}
        curA=headA
        curB=headB
        while curA or curB:
            if curA:
                if curA in harshmap:
                    return curA
                else:
                    harshmap[curA]=True
                curA=curA.next
            if curB:
                if curB in harshmap:
                    return curB
                else:
                    harshmap[curB]=True
                curB=curB.next
        return curA