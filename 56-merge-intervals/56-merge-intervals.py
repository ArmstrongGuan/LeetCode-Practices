class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output=[]
        low, high=intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<= high:
                high=max(high, intervals[i][1])
            else:                
                output+=[[low, high]]
                low, high=intervals[i][0], intervals[i][1]
        output+=[[low, high]]
        return(output)
        