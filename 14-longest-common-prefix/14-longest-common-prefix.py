class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[0]
        common=0
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j])<i+1 or a[i] != strs[j][i]:
                    return(strs[0][:common])
            common=common+1
        return(strs[0][:common])
            