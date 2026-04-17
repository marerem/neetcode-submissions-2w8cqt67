class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_s, new_end = newInterval
        result = []
        placed = False
        for start, end in intervals:
            if new_s > end:#add all before copletyl before
                result.append([start,end])
            elif start > new_end:#add complaety after
                if not placed:
                    result.append([new_s, new_end])
                result.append([start,end])
                placed = True
            else:
                new_end = max(end,new_end)
                new_s = min(start,new_s)
        if not placed:
           result.append([new_s, new_end])
        return result
