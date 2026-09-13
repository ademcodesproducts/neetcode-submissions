from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # value -> count

        bucket = defaultdict(list)
        for v, c in freq.items():
            bucket[c].append(v)
        
        result = []
        for count in range(len(nums), 0, -1):
            if count in bucket.keys():
                result.extend(bucket[count])
            if len(result) == k:
                break
        return result