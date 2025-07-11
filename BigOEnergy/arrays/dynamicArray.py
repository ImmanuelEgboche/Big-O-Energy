class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None * capacity]
        self.size = 0
        


    def get(self, i: int) -> int:
        if i < self.size:
            return self.arr[i]
        return "Out of range"


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = n
        self.size +=1 

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Array is empty")
        
        last = self.arr[self.size -1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return last

    def resize(self) -> None:
       self.capacity =  2*self.capacity
       new_arr = [None] * self.capacity

       for i in range(self.size):
           new_arr = self.arr[i]
       self.arr = new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
