class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store key value : key is anagrmam and value is a list
        store = defaultdict(list)
    
        for word in strs:
            anagram = [0]*26
            for w in word:
                index = ord("a") - ord(w)
                anagram[index] += 1
            store[tuple(anagram)].append(word)
        return list(store.values())
sol = Solution()
assert sol.groupAnagrams(["act","pots"]) == [["act"],["pots"]]

