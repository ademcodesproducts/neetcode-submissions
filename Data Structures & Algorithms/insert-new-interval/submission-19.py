class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        prev_interval = prev_end <= start of the newInterval
        
        # O(n) -> finding where to isnert
        # O(1) -> overlap
        # O(n) -> if overlap merge intervals
        """

        # curr_interval before newInternal, after it or overlapping it
        # prev_end of curr_inteval < start of newInterval
        # end of newInterval < prev_start of curr_interval
        # prev_end of curr_interval >= start of newInterval

        result = []
        inserted = False

        for start, end in intervals:
            
            # curr_interval < newInterval
            if end < newInterval[0]:
                result.append([start, end])

            #newInterval < curr_interval
            elif newInterval[1] < start:
                if inserted == False:
                    result.append(newInterval)
                    inserted = True
                result.append([start, end])

            # curr_interval and newInterval overlap
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
                
        if inserted == False:
            result.append(newInterval)
        
        return result