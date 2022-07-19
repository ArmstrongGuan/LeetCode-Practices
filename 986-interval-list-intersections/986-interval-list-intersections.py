class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        output=[]
        while i<len(firstList) and j<len(secondList):
            if firstList[i][0]> secondList[j][1]:
                j=j+1
                continue
            if firstList[i][1]< secondList[j][0]:
                i=i+1
                continue
            low=max(firstList[i][0], secondList[j][0])
            high=min(firstList[i][1], secondList[j][1])
            output.append([low, high])
            if high==firstList[i][1]:
                i=i+1
            if high==secondList[j][1]:
                j=j+1
        return output