class Solution:
    def numSquares(self, n: int) -> int:
        #a theorem claims that the maxmal result is 4
        if n==0:
            return 0
        result=[4]*(n+1)
        for i in range(1,int(sqrt(n))+1):
            result[i**2]=1
        count =2
        while result[n]==4 and count <4:
            for i in range(n,1,-1):
                if result[i]==4:
                    for j in range(1,int(sqrt(i))+1):
                        if result[i-j**2]==count-1:
                            result[i]=count
                            break
            count+=1
        return result[n]
        