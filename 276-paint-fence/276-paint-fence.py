class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n<3:
            return k**n
        #k* (k-1)**(number of partitions-1) is the number of ways for each partition
        #
        #return self.numWays(n-1, k)*(k-1)+self.numWays(n-2, k)*(k-1)
        result = [1]* (n+1)
        result[1]=k
        result[2]=k**2
        for i in range(3,n+1):
            result[i]=(result[i-1]+result[i-2])*(k-1)
        return result[n]
            