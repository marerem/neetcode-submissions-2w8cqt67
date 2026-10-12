class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ == 0:
                    pairs.add((nums[i],nums[l],nums[r]))
                    l +=1
                    r -= 1
                elif sum_ < 0:
                    l += 1
                elif sum_ > 0:
                    r -= 1
        return list(pairs)
                
                 
