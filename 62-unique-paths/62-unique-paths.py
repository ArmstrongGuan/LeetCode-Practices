class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map={}
        def count(m,n,map):
            if m==1 or n==1:
                return(1, map)
            if (m,n) in map:
                return(map[m,n], map)
            else:
                map[m,n]=count(m-1,n,map)[0]+count(m,n-1,map)[0]
                map[n,m]=map[m,n]
                return map[m,n], map
        return count(m,n, map)[0]
        