"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        min_heap, room = [], 0

        for interval in intervals:
            heapq.heappush(min_heap, interval.end)
            end = min_heap[0]
            if end > interval.start:
                room += 1
            else:
                heapq.heappop(min_heap)
            
        return room