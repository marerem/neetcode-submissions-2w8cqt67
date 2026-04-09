class Solution:
    def groupAnagrams(self, strs: list[str]) -> List[List[str]]:
        store = defaultdict(list) # key anagram : value is list of thess words
        for word in strs:
            anagram = [0]*26
            for w in word:
                index = ord("a") - ord(w)
                anagram[index] += 1
            store[tuple(anagram)].append(word)
        return list(store.values())
sol = Solution()
assert sol.groupAnagrams(["act","pots"])  == [["act"],["pots"]]