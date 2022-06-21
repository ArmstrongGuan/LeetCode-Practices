class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        length={}
        maximum=1
        for k in range(len(nums)):
            i=nums[k]
            if i in length: continue
            #print(i)
            if i+1 in length and i-1 in length:
                a=1+length[i-1]+length[i+1]
                length[i-length[i-1]], length[i+length[i+1]] = a , a
                length[i]=1
                maximum=max(maximum, a)
            elif i+1 in length:
                a=1+length[i+1]
                length[i], length[i+length[i+1]]= a,a
                maximum=max(maximum, a)
            elif i-1 in length:
                a=1+length[i-1]
                length[i-length[i-1]], length[i] = a,a
                maximum=max(maximum, a)
            else:
                length[i]=1
            #print(length, maximum)
        return maximum