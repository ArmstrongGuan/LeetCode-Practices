class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        output=[]
        cur=0
        for i in range(len(strs)):
            b=''.join(sorted(strs[i]))
            if b in map:
                output[map[b]]+=[strs[i]]
            else:
                map[b]=cur
                output+=[[strs[i]]]
                cur+=1
        return(output)
                