a=1
b=2
c=3

d=a+b+c

print(d)

nome="torreta, o brabo"

print(nome[1:5])

print("t" in nome)
print("z" in nome)

array=[0,1,2,3,4,5,"torreta"]
array.append(7)

print(array)

print(array.index("torreta"))

array.append(1)

print(array.count(1))

array.reverse()

array.remove(1)

array.reverse()
print(array)

array2=[1,6,12,7,81]
array2.sort()

print(array2)

telefones={"tiago":512312,"diogo":518293123,"marta":51829387123}
telefones["rita"]=95819283
del telefones["diogo"]
print(telefones)

tupla=("react","python","udemy")

print(tupla[0:2])

print(len(tupla))

print(tupla*3)

print("udemy" in tupla)

listamaneira=[1,2,3]
tuplamaneira=tuple(listamaneira)

print(tuplamaneira)

number=2

if(number==1):
  print("numero é 1 :O")
else:
  print("numero n é 1 :(")

nomemaneiro = "Torreta"
# if(){}else if(){}else{}

if("z" in nomemaneiro):
  print("o nome tem z")
elif("o" in nomemaneiro):
  print("o nome tem o")
else:
  pass

# for(let x = 0;x < 5; x++)
for x in range(0,5):
  print(f'Valor de x é {x}')
  # for


nomemaismaneiro="torretex"

for letra in nomemaismaneiro:
  print(letra)
  # for in

listamaismaneira=[1,2,3]

for n in listamaismaneira:
  print(n)
  # for in

numeromaismaneiro=15

while(numeromaismaneiro>0):
  print(numeromaismaneiro)
  numeromaismaneiro=numeromaismaneiro-1
  # while padrão

nx = 20

while True:
  nx=nx-1
  print(nx)
  if(nx==4):
    continue
    # reinicia o ciclo
  if(nx==2):
    break
    # quebra o ciclo

for x in range(0,5):
  pass
  # passa, tipo o return la

