class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groupSizesOri=groupSizes.copy()
        groupSizes.sort()
        ans=[[]]
        k=0
        i=0
        while i<len(groupSizes):
            if i>=1:
                ans.append([])
            for j in range(groupSizes[i]):
                ans[k].append(groupSizesOri.index(groupSizes[i+j]))
                groupSizesOri[groupSizesOri.index(groupSizes[i+j])]=0
            i+=groupSizes[i]
            k+=1
        return ans
pass

solu=Solution()
groupSizes = [2,1,3,3,3,2]
print(solu.groupThePeople(groupSizes))