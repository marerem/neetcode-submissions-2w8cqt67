class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        fr_count = [[] for i in range(len(nums)+1)]
        for num, fr in count.items():
            fr_count[fr].append(num)

        for i in range(len(nums),-1,-1):
            for n in fr_count[i]:
                res.append(n)
                if len(res) == k:
                    return res
                


