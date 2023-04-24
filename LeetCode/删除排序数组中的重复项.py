class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:]=sorted(list(set(nums)))
        return len(nums)
pass

nums=[-1,0,0,1,1,1,2,2,3,3,4]
solu=Solution()
print(solu.removeDuplicates(nums))