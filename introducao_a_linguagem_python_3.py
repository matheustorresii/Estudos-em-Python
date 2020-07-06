import random

n = random.randint(0, 10)

array = [10,20,30]

number = random.choice(array)

a = 10
b = 0

try:
  print(a/b)
except:
  print(f'dividido por 0')

print(number)