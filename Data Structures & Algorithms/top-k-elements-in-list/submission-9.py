class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums) # 5 : 3
        l = sorted(store.items(),key = lambda x: x[1], reverse = True)
        return [i[0] for i in l[:k]]