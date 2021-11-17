class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=[-10**6]+nums1+[10**6]
        nums2=[-10**6]+nums2+[10**6]
        l1=len(nums1)
        l2=len(nums2)
        mid_b=0
        mid_s=0
        count1=0
        count2=0
        count=0
        #if not nums1:
        #    return(nums2[(l2-1)//2] if (l2 % 2) else (nums2[l2//2]+nums2[l2//2-1])/2)
        #if not nums2:
        #    return(nums1[(l1-1)//2] if (l1 % 2) else (nums1[l1//2]+nums1[l1//2-1])/2)
        while count<=(l1+l2)/2:
            if nums1[count1]<=nums2[count2]:
                mid_b, mid_s= nums1[count1], mid_b
                count1=count1+1
            else:
                mid_b, mid_s= nums2[count2], mid_b
                count2=count2+1
            count=count+1
        return( mid_b if (l1+l2)%2 else (mid_b+mid_s)/2)
            