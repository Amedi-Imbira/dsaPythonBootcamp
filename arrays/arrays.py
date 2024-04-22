class Array:
      def __init__(self) -> None:
            self._length = 0
            self._capacity = 1
            self._A = [None] * self._capacity
            
      def __len__(self) -> int:
            return self._length
      
      def __getitem__(self, i):
            return self._A[i]
      
      def __setitem__(self, i, val):
            self._A[i] = val
      
      def append(self, val):
            if self._length == self._capacity:
                  self._resize()
            
            self._A[self._length] = val
            self._length += 1
            
      def pop(self):
            self._A[self._length-1] = None
            self._length -= 1
                  
      def _resize(self):
            self._capacity = self._capacity * 2
            B = [None] * self._capacity
            
            for j in range(self._length):
                  B[j] = self._A[j]
                  
            self._A = B
            
      def __str__(self) -> str:
            return str(self._A)[::1]
            
a = Array()
a.append(2)
a.append(3)
a.append(5)
a.append(7)

a.pop()

print(a)