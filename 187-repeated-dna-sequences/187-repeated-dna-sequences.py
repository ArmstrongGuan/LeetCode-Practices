class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result=[]
        harshmap={}
        for i in range(len(s)-9):
            if s[i:i+10] in harshmap:
                if harshmap[s[i:i+10]]==False:
                    result.append(s[i:i+10])
                    harshmap[s[i:i+10]]=True
            else:
                harshmap[s[i:i+10]]=False
        return result