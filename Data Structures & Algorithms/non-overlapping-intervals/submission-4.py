class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ''' 
        1. Sort intervals by end time.
        2. Keep the interval with the earliest end.
        3. If the next interval overlaps, 
               remove the CURRENT interval.
        4. Count removals.
        '''
        intervals.sort(key=lambda x: x[1])
        res = 0

        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if prevEnd > start:
                res += 1
            else:
                prevEnd = intervals[i][1]
        return res