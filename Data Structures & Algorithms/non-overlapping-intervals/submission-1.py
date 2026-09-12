class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ''' 
        1. Sort intervals by end time.
        2. Keep the interval with the earliest end.
        3. If the next interval overlaps, 
               remove the CURRENT interval.
        4. Count removals.
        '''
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        removals = 0
        groupInterval = [intervals[0]]

        def overlap(iv_1, iv_2):
            start = max(iv_1[0], iv_2[0])
            end = min(iv_1[1], iv_2[1])
            return end - start > 0

        for interval in intervals[1:]:
            if overlap(interval, groupInterval[-1]):
                removals += 1
            else:
                groupInterval.append(interval)
        
        return removals