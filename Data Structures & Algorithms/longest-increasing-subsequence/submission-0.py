from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        for val in nums[1:]:
            ind = bisect_left(tail, val) #find the first number in tails that is >= x
            if ind == len(tail):#
               tail.append(val)
            else:
                tail[ind] = val #Why replace?Because [2, 3, 7] is better than [2, 5, 7] for future growth. A smaller middle number gives more chance to extend
        return len(tail)