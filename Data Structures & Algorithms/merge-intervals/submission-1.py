class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. iterate over interval <- for loop
        # 2. check if overlap <- start, end pointer
        # 3. merge overlapping intervals <- for every [start, end] pair create new interval

        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            secInterval = result[-1]
            start = max(interval[0], secInterval[0])
            end = min(interval[1], secInterval[1])
            if end - start >= 0:
                newInterval = [min(interval[0], 
                    secInterval[0]), max(interval[1], secInterval[1])]
                result[-1] = newInterval
            else:
                result.append(interval)    
        return result