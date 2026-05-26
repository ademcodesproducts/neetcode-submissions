class TimeMap:

    def __init__(self):
        self.key_value_store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        kv_arr = self.key_value_store[key]

        if not kv_arr:
            return ''

        timestamp_val = ''
        l, r = 0, len(kv_arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if kv_arr[mid][0] <= timestamp:
                timestamp_val = kv_arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return timestamp_val
            