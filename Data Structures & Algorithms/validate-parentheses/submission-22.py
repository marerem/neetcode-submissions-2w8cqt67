class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        map_ = {')':'(','}':'{',']':'['}
        tmp = []# keep opens [[
        for i in s:
            if i not in map_: #open
                tmp.append(i)
            elif i in map_ and tmp:
                if map_[i] == tmp[-1]:
                    tmp.pop()
                else:
                    return False
            else:
                return False
        return True if not tmp else False
      
       