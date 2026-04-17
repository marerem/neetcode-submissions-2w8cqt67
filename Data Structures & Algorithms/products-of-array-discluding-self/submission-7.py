class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1]*len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            prefix_sum[i] *= prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            prefix_sum[i] *= postfix
            postfix *= nums[i]
        return prefix_sum