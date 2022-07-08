class Solution:
    def hammingWeight(self, n: int) -> int:
        cur=0
        while n>0:
            cur+=n%2
            n=n//2
        return cur