class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[[]]
        cur=-11
        length=0
        for i in nums:
            if i==cur:
                length+=1
            else:
                for j in range(len(result)-1, -1, -1):
                    for k in range(length):
                        result.append(result[j]+[cur]*(k+1))
                length=1
                cur=i
        for j in range(len(result)-1, -1, -1):
            for k in range(length):
                result.append(result[j]+[cur]*(k+1))
        return result
                