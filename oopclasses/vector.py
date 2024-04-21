class Vector:
      def __init__(self, d):
            self._coords = [0] * d
            
      def __len__(self):
            return len(self._coords)
      
      def __getitem__(self, i):
            return self._coords[i]
      
      def __setitem__(self, i, val):
            self._coords[i] = val
            
      def __add__(self, other):
            if len(self) != len(other):
                  raise ValueError('Dimensions must be equal')
            
            result = Vector(len(self))
            for j in range(len(self)):
                  result[j] = self[j] + other[j]
            return result
      
      def __eq__(self, other):
            return self._coords == other._coords
      
      def __ne__(self, other):
            return not self == other
      
      def __str__(self):
            return '<' + str(self._coords)[1:-1] + '>'
      
v1 = Vector(3)
print(v1)