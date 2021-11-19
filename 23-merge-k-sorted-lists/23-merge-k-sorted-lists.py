# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Should use heap for the easiest way. Must have a try when have time.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists==[]:
            return(ListNode().next)
        cur=[]
        for i in range(len(lists)):
            if lists[i]:
                cur+=[lists[i].val]
            else:
                cur+=[10**4]
        if min(cur)==10**4:
            return(None)
        m=min(cur)
        start=cur.index(m)
        output=ListNode()
        dummy=output
        while m< 10**4:
            for i in range(len(lists)):
                if lists[i] and lists[i].val==m:
                    dummy.next=ListNode(m)
                    dummy=dummy.next
                    lists[i]=lists[i].next
                    cur[i]= (lists[i].val if lists[i] else 10**4)
            m=min(cur)
        return output.next
        
        # dummy= ListNode()
        # cur=0
        # map={}
        # control=0
        # while control < len(lists):
        #     if cur in map:
        #         print(cur)
        #         for j in range(len(map[cur])):
        #             dummy.val= cur
        #             dummy.next=ListNode()
        #             lists[map[cur][j]]=lists[map[cur][j]].next
        #             if lists[map[cur][j]]:
        #                 map[lists[map[cur][j]].val] += [map[cur][j]]
        #     else:
        #         for i in range(len(lists)):
        #             if lists[i].val in map:
        #                 map[lists[i].val] +=[i]
        #             else:
        #                 map[lists[i].val] =[i]
        #     control=0
        #     for i in range(len(lists)):
        #         if lists[i]:
        #             control+=1
        # return dummy