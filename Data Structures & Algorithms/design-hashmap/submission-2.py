class MyHashMap:

    def __init__(self):
        self.data = []
        
    def put(self, key: int, value: int) -> None:
        while len(self.data) <= key:
            self.data.append(-1)
        self.data[key] = value
        
    def get(self, key: int) -> int:
        if key >= len(self.data):
            return -1
        return self.data[key]

    def remove(self, key: int) -> None:
        if key < len(self.data):    
            self.data[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)