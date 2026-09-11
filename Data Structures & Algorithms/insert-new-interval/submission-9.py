class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1. Check where new interval belongs <- for loop over interval[0]O(n)
        # 2. Insert interval <- O(1) 
        # 3. Merge interval O(n)
        '''
        3.1 Loop all intervals O(n)
        3.2 check if overlap O(1)
        3.3 replace interval if overlap exists O(1)
        '''
        
        def overlap(iv_1, iv_2):
            start = max(iv_1[0], iv_2[0])
            end = min(iv_1[1], iv_2[1])
            return end - start >= 0

        for i in range(len(intervals)): 
            if intervals[i][0] > newInterval[0]: # Check edge case if ==
                intervals.insert(i, newInterval)
                break
                
        if newInterval not in intervals:
            intervals.append(newInterval)

        result = [intervals[0]] if len(intervals) > 0 else []
        for interval in intervals[1:]:
            secInterval = result[-1]
            if overlap(interval, secInterval):
                merged = [
                    min(interval[0], secInterval[0]),
                    max(interval[1], secInterval[1]),
                ]
                result[-1] = merged
            else:
                result.append(interval)

        return result if len(intervals) > 0 else [newInterval]