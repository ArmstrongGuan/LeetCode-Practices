class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #the only way of O(n) time and O(1) space is XOR
        #XOR is commutative and associative 类似于对称差
        a=0
        for i in nums:
            a=a^i
        return a