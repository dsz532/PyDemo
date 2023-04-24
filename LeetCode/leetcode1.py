from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums))[i+1:]:
                if nums[i]+nums[j]==target:
                    result=[i,j]
                    return result
    pass
nums = [3,3]
target = 6
solution=Solution()
result=solution.twoSum(nums,target)
print(result)