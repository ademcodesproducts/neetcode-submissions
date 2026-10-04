class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. iterate over interval <- for loop
        # 2. check if overlap <- start, end pointer
        # 3. merge overlapping intervals <- for every [start, end] pair create new interval
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = result[-1][1]
            if start <= prev_end:
                merged_end = max(prev_end, end)
                result[-1][1] = merged_end
            else:
                result.append([start, end])
        return result