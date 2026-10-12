class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store key () n) : value (index of n)
        resid_store = {}
        for i in range(len(nums)):
            resid = target - nums[i]
            if resid in resid_store:
                return [resid_store[resid], i]
            resid_store[nums[i]] = i



        

            