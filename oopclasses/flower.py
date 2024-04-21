from dataclasses import dataclass

@dataclass
class Flower:
      _name: str
      _petals_num: int
      _price: float
      
      @property
      def name(self) -> str:
            return self._name.capitalize()
      
      @property
      def petals(self) -> int:
            return self._petals_num
      
      @property
      def price(self) -> float:
            return f'${self._price}'
      
      @name.setter
      def name(self, val: str) -> None:
            if not isinstance(val, str):
                  raise TypeError('Name should be a string')
            
            self._name = val
            
      @petals.setter
      def petals(self, val: int) -> None:
            if not isinstance(val, int):
                  raise TypeError('Number of petals must be a whole number')
            elif val < 0:
                  raise ValueError('Number of petals cannot be negative')
            
            self._petals_num = val
            
      @price.setter
      def price(self, val: float) -> None:
            if not isinstance(val, float):
                  raise TypeError('Price must be numerical')
            elif val < 0:
                  raise ValueError('Price cannot be negative')
            
            self._price = val