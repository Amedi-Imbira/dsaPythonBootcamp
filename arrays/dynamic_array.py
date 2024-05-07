# FIXME: No means for shrinking the size of the underlying array when 
# elements are popped from list
# FIXME: Does not support the use of negative indices

class Array:
      def __init__(self):
            self._length = 0
            self._capacity = 1
            self._A = [None] * self._capacity
            
      def __len__(self):
            return self._length
      
      def __getitem__(self, i):
            if not isinstance(i, int):
                  raise TypeError('array indices must be integers or slices, not str')
            
            if i < 0:
                  i += self._length
                  
            if not 0 <= i < self._length:
                  
                  raise IndexError('array index out of range')
            
            return self._A[i]
      
      def __setitem__(self, i, val):
            if not 0 <= i < self._length:
                  raise IndexError('array index out of range')
            
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
            self._capacity *= 2
            B = [None] * self._capacity
            
            for j in range(self._length):
                  B[j] = self._A[j]
                  
            self._A = B
            
      def __str__(self):
            
            return str(self._A)[::1]
            
primes = Array()
primes.append(2)
primes.append(3)
primes.append(5)

# primes.pop()

print(primes)