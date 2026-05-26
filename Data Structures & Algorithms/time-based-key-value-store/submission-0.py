class TimeMap:

    def __init__(self):
        self.key_value_store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not self.key_value_store[key]:
            return ''

        timestamp_prev = 0
        timestamp_val = ''

        for pair in self.key_value_store[key]:
            if pair[0] <= timestamp and pair[0] > timestamp_prev:
                timestamp_prev = pair[0]
                timestamp_val = pair[1]
        return timestamp_val
            