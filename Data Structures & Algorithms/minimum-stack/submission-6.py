class MinStack:

    def __init__(self):
        self.data = []
        self.min_data = []
        
    def push(self, val: int) -> None:
        self.data.append(val)
        val = min(val, self.min_data[-1] if self.min_data else val)
        self.min_data.append(val)
        
        
    def pop(self) -> None:
        self.data.pop()
        self.min_data.pop()

    def top(self) -> int:
        return self.data[-1]
        
    def getMin(self) -> int:
        return self.min_data[-1]