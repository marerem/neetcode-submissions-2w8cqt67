class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr_max = nums[0]
        for i in nums[1:]:
            curr_max = max(i, curr_max + i)
            best = max(best,curr_max)
        return best