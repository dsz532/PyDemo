class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        addlist=nums1+nums2
        addlist.sort()
        if len(addlist)%2==0:
            i=len(addlist)/2
            j=len(addlist)/2-1
            ans=(addlist[int(i)]+addlist[int(j)])/2
        else:
            i=(len(addlist)-1)/2
            ans=addlist[int(i)]
        return ans
pass
sulo=Solution()
nums1 = [1,3]
nums2 = [2]
print(sulo.findMedianSortedArrays(nums1,nums2))