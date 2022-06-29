class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        m=math.gcd(n,k)
        for i in range(m):
            cur=i
            for j in range(n//m -1):
                nums[cur], nums[(cur-k) % n]= nums[(cur-k )% n], nums[cur]
                cur=(cur-k) % n
                
                