class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums) # 5 : 3
        freq = [[] for i in range(len(nums)+1)] #max freuqent number can be all number the same so it will be same number as length of nums
        for num, fq in store.items(): #(5,3)
            freq[fq].append(num)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res