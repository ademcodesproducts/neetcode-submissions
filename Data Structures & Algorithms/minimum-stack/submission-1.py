class MinStack:

    def __init__(self):
        self.data = []
        
    def push(self, val: int) -> None:
        self.data.append(val)
        
    def pop(self) -> None:
        self.data.pop()
        

    def top(self) -> int:
        return self.data[len(self.data) - 1]
        
    def getMin(self) -> int:
        min_elem = float('inf')
        for e in self.data:
            min_elem = min(min_elem, e)
        return min_elem
