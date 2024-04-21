class Vector:
      def __init__(self, d) -> None:
            self._coords: list[int] = [0] * d
            
      def __len__(self) -> int:
            return len(self._coords)
      
      def __getitem__(self, i):
            return self._coords[i]
      
      def __setitem__(self, i, val) -> None:
            self._coords[i] = val
            
      def __add__(self, other: list[int]) -> list[int]:
            if len(self) != len(other):
                  raise ValueError('Dimensions must be equal')
            
            result = Vector(len(self))
            
            for j in range(len(self)):
                  result[j] = self[j] + other[j]
            return result
      
      def __sub__(self, other: list[int]) -> list[int]:
            if len(self) != len(other):
                  raise ValueError('Dimensions must agree')
            
            result = Vector(len(self))
            
            for j in range(len(self)):
                  result[j] = self[j] - other[j]
                  
            return result
      
      def __neg__(self):
            result = Vector(len(self))
            
            for j in range(len(self)):
                  result[j] = -self[j]
            
            return result
      
      def __eq__(self, other):
            return self._coords == other._coords
      
      def __ne__(self, other):
            return not self == other
      
      def __str__(self):
            return '<' + str(self._coords)[1:-1] + '>'
      
v1 = Vector(3)
v1[0] = 8
v1[1] = 3
v1[2] = 5
# print(v1)

v2 = Vector(3)
v2[0] = 1
v2[1] = 2
v2[2] = 3

print('Substract: ', v1 - v2)
print('Add: ', v1 + v2)
print('Negate: ', -v1)
