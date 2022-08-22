class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #based on approach 4 in solution
        intervals.sort()
        pointer=intervals[0]
        output=0
        for i in range(1, len(intervals)):
            cur=intervals[i]
            if cur[0]>=pointer[1]:
                pointer=cur
                continue
            elif cur[1]<=pointer[1]:
                pointer=cur
                output+=1
            else:
                output+=1
        return output
            