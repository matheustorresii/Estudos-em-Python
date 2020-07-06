x = [1,2,3,4,5]
# y = []

# for i in x:
#   y.append(i**2)

y = [i**2 for i in x]

print(y)

z = [i for i in x if i%2 == 1]

print(z)



lista = ["abacate", "bola", "cachorro"]

# for i in range(len(lista)):
#   print(i, lista[i])

for i, nome in enumerate(lista):
  print(i, nome)



def dobro(x):
  return x*2

valor = [1,2,3,4,5]

# print(dobro(valor))
valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)

print(valor_dobrado)



from functools import reduce

def soma(x, y):
  return x+y

lista_daora = [1,3,5,10,20]

soma = reduce(soma, lista_daora)

print(soma)



lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "chacorro", "dinheiro", "elefante"]
lista3 = ["R$ 2,00","R$ 15,00","R$ 0,00","R$ 1,00","R$ 50,00"]

for numero, nome, valor in zip(lista1,lista2,lista3):
  print(numero, nome, valor)

print("*******\n ***** \n  ***  \n   *   ")
