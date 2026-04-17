class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for start_cur, end_cur in intervals[1:]:
            if start_cur > end:
                res.append([start, end])
                start = start_cur
                end = end_cur
            if end_cur >= end:
                end = end_cur
            if start_cur < start:
                start = start_cur
        res.append([start, end])
        return res
  