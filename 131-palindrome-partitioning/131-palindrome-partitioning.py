class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s=="":
            return [[]]
        result=[]
        for i in range(1,len(s)+1):
            if s[:i]==s[i-1::-1]:
                result=result+ [[s[:i]]+rest for rest in self.partition(s[i:])]
        return result
         
        #https://leetcode.com/problems/palindrome-partitioning/discuss/42025/1-liner-Python-Ruby
        #based on the above solution:
        #def partition(self, s):
        #    return [[s[:i]] + rest
        #            for i in xrange(1, len(s)+1)
        #            if s[:i] == s[i-1::-1]
        #            for rest in self.partition(s[i:])] or [[]]
                

                