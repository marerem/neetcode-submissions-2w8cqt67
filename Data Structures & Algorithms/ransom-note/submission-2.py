class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        store = [0]*26
        for m in magazine:
            store[ord("a") - ord(m)] += 1
        for n in ransomNote:
            if store[ord("a") - ord(n)] == 0:
                return False
            store[ord("a") - ord(n)] -= 1
        
        return True

sol = Solution()
assert sol.canConstruct("aa", "aaa") == True