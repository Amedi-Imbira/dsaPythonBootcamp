from dataclasses import dataclass

@dataclass
class CreditCard:
      _customer: str
      _bank: str
      _account: str
      _limit: int
      _balance: float = 0
      
      @property      
      def customer(self):
            return self._customer
      
      @property
      def bank(self):
            return self._bank
      
      @property
      def account(self):
            return self._account
      
      @property
      def limit(self):
            return self._limit
      
      @property
      def balance(self):
            return self._balance
      
      def charge(self, price):
            if self._balance + price > self._limit:
                  return False
            else:
                  self._balance += price
                  
      def make_payment(self, amount):
            self._balance -= amount
            
cc = CreditCard('John Bowman', 'Carlifonia Savings', '2345 1232 4576 8787', 1000)
print(cc)
            