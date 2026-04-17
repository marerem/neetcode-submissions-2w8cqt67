class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        result = []
        i, n = 0, len(intervals)
        #1add first not overlappign interval
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1
        #2.merge and insert new
        while i < n and intervals[i][0] <= new_end:#next interval start less then new end
              new_end = max(intervals[i][1], new_end)
              new_start = min(intervals[i][0], new_start)
              i += 1
        result.append([new_start,new_end])
 
        #3. add residual
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result

