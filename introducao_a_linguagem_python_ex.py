def maior_de_idade(idade):
  if idade >= 18:
    print(f'maior de idade')
  else:
    print(f'menor de idade')

maior_de_idade(25)

def cria_lista(array):
  array.sort()
  print(array)

cria_lista([79,5,7])

import math

def bhaskara(a, b, c):
  delta = (b**2) - 4*a*c
  x1 = (-b + math.sqrt(delta))/(2*a)
  x2 = (-b - math.sqrt(delta))/(2*a)
  print(x1, x2)

bhaskara(3, -7, 4)

def operator(x, y, operator):
  if operator == "+":
    print(x + y)
  elif operator == '-':
    print(x - y)
  elif operator == "/":
    print(x / y)
  elif operator == "*":
    print(x * y)
  else:
    print(f'sinal não suportado :/')

operator(1,1,"/")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
 
media = (nota1+nota2)/2
 
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
