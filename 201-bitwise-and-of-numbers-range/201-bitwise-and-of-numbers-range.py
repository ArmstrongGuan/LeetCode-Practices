class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # see solution
        # the key is the result will be the common prefix
        shift = 0   
        # find the common 1-bits
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift