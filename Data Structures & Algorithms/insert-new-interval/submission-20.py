class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        is_merged = False
        for start, end in intervals:
            if not is_merged and newInterval[1] < start:
                merged.append(newInterval)
                merged.append([start, end])
                is_merged = True
            elif is_merged or end < newInterval[0]:
                merged.append([start, end])
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        if not is_merged:
            merged.append(newInterval)

        return merged

    