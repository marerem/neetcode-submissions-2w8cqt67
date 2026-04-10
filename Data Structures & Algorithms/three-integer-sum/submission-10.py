class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_ = nums[l] + nums[r] + nums[i]
                if sum_ < 0:
                    l += 1
                elif sum_ > 0:
                    r -=1
                else:
                    res.add((nums[l],nums[r],nums[i]))
                    l += 1
                    r -= 1
        return [list(r) for r in res]




            