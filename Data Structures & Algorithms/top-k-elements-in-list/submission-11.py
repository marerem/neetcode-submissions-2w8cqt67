class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums) # {1:1, 2:2, 3:3}
        frq = [[] for i in range(len(nums)+1)]
        for n, fr in store.items():
            frq[fr].append(n)
        print(frq)
        res = [] #len(res) ==k
        for i in frq[::-1]:
            for n in i:
                res.append(n)
                if len(res) == k:
                    return res