from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.queue = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.queue.remove(key)
        self.queue.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
            return

        if len(self.cache) >= self.capacity:
            pop_key = self.queue.popleft()
            self.cache.pop(pop_key)

        self.cache[key] = value
        self.queue.append(key)

