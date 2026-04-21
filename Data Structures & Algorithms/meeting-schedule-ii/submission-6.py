"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort them, merge them, len of merg intervals numbe for rooms
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        minheap = []
        for interval in intervals:
            
            # free up a room if the earliest meeting has ended
            if minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)
            # use a room for the current meeting
            heapq.heappush(minheap, interval.end)
            print(minheap)
        return len(minheap)
            
  
