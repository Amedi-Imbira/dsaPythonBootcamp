from dataclasses import dataclass

@dataclass
class CreditCard:
      """
      Represents a credit card
      """
      _customer: str
      _bank: str
      _account: str
      _limit: int
      _balance: float = 0
      
      @property      
      def customer(self) -> str:
            return self._customer
      
      @property
      def bank(self) -> str:
            return self._bank
      
      @property
      def account(self) -> str:
            return self._account
      
      @property
      def limit(self) -> int:
            return self._limit
      
      @property
      def balance(self) -> float:
            return self._balance
      
      def charge(self, price: float):
            """
            Method to process credit card payments
            FIXME: The method can either return a boolean or 
            do the calculation
            """
            if self._balance + price > self._limit:
                  return False
            else:
                  self._balance += price
                  
      def make_payment(self, amount) -> None:
            """
            Method to process reducing the credit card balance
            """
            if not isinstance(amount, (int, float)):
                  raise TypeError('Amount must be numerical')
            elif amount < 0:
                  raise ValueError('Amount cannot be negative')
            
            self._balance -= amount
            
cc = CreditCard('John Bowman', 'Carlifonia Savings', '2345 1232 4576 8787', 1000)
print(cc)
            