class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        count = defaultdict(int)
        l = 0
        max_f = 0
        for r, ch in enumerate(s):
            count[ch] += 1
            max_f = max(max_f,count[ch])
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            best = max(best,r - l + 1)
        return best

        


