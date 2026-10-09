class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store = defaultdict(int)
        for i in range(len(s)):
            store[s[i]] +=1
            store[t[i]] -=1
        return all(value == 0 for value in store.values())