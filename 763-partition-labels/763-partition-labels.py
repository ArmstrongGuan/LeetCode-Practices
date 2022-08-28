class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        harshmap={}
        for i in range(len(s)):
            if s[i] in harshmap:
                harshmap[s[i]][1]=i
            else:
                harshmap[s[i]]=[i,i]
        result=[]
        start=0
        end=harshmap[s[start]][1]
        while True:
            check=False
            for interval in harshmap.values():
                if start<=interval[0]<=end:
                    if interval[1]>end:
                        end=interval[1]
                        check=True
                        break
            if check==False:
                result.append(end-start+1)
                start=end+1
                if start<len(s):
                    end=harshmap[s[start]][1]
                    continue
                else:
                    break
        return result
                        