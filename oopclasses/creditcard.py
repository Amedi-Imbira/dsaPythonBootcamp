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
            first, last = self._customer.split(' ')
            return f'{first.capitalize()} {last.capitalize()}'
      
      @property
      def bank(self) -> str:
            #FIXME: what if bank has three names. How can we make it dynamic
            first, second = self._bank.split(' ')
            return f'{first.capitalize()} {second.capitalize()}'
      
      @property
      def account(self) -> str:
            return self._account
      
      @property
      def limit(self) -> int:
            return f'${self._limit}'
      
      @property
      def balance(self) -> float:
            return f'${self._balance}'
      
      def _can_pay(self, price: float) -> bool:
            if self._balance + price > self._limit:
                  return False
            else:
                  return True
      
      def charge(self, price: float):
            """
            Method to process credit card payments
            FIXME: The method can either return a boolean or do the calculation
            """
            if self._can_pay(price):
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

if __name__ == '__main__':            
      cc = CreditCard('john bowman', 'Carlifonia Savings', '2345 1232 4576 8787', 1000)
      print(cc.bank)
            