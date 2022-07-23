class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        starts=[0]
        for i in range(len(s)):
            for j in starts:
                if s[j:i+1] in wordDict:
                    starts.append(i+1)
                    break
        if starts[-1]==len(s):
            return True
        else:
            return False