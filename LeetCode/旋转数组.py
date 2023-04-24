class Solution:
    def rotate(self, nums: list[int], k: int) -> list:
        if k<len(nums):
            nums[:] = nums[len(nums)-k:len(nums):1] + nums[0:len(nums)-k:1]
        else:
            k=k%len(nums)
            nums[:] = nums[len(nums) - k:len(nums):1] + nums[0:len(nums) - k:1]
        return nums


pass

nums=[1,2]
k=3
solu=Solution()
print(solu.rotate(nums,k))