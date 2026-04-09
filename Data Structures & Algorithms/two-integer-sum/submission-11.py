class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_res = defaultdict(list)
        for i, n in enumerate(nums):
            res = target - n
            if res in store_res:
                return [store_res[res][0],i]
            store_res[n].append(i)
            