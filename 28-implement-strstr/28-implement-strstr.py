class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        if len(haystack)< len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                print(i)
                if haystack[i:i+len(needle)]==needle:
                    return(i)
        return -1