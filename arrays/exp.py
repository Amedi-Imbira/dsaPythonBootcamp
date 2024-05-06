import sys

# data = []

# for k in range(25):
#       a = len(data)
#       b = sys.getsizeof(data)
      
#       print(f'Length = {a} || Capacity reserved = {b}')
#       data.append(None)
      
      
# Trial one = IndexError: pop from empty list

primes = [2, 3, 5, 7, 11, 13, 17, 19, 29, 31, 37, 29, 41]

for k in range(len(primes)):
      a = len(primes)
      b = sys.getsizeof(primes)
      
      print(f'Length = {a} || Capacity = {b}')
      primes.pop()