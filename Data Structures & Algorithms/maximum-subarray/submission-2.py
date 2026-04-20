class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = best_max = nums[0]
        for i in nums[1:]:
            curr_max = max(i, curr_max + i)
            best_max = max(best_max, curr_max)
        return best_max