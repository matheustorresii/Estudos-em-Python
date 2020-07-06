def soma(x, y):
  return x + y

def multiplicacao(x, y):
  return x * y

s = soma(2, 2)
m = multiplicacao(2, 2)

print(soma(s, m))

arquivo = open("arquivo.txt")

# transforma em array
linhas = arquivo.readlines()

for linha in linhas:
  print(linha)

# texto direto
linhas = arquivo.read()
print(linhas)

# cria arquivo
w = open("arquivo2.txt", "w")

# escreve naquele arquivo
w.write("Esse é o meu arquivo")

w.close()

# escreve no arquivo sem sobrescrever ele
a = open("arquivo.txt", "a")

a.write("\netapora")

a.close()

array_maneiro = ["maçã", "uva", "pêra", "salada mista"]

if "uva" in array_maneiro:
  print(f'tem uva la')
else:
  print(f'não tem uva la')

lista_maneira = [612,612,787,1,81,6,1,71,7]

lista_maneira.sort(reverse=True)

print(lista_maneira)

dicionario_maneiro = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

print(dicionario_maneiro["A"])

# for pra cada chave do dicionario
for chave in dicionario_maneiro:
  print(dicionario_maneiro[chave])

# retorna tupla
for i in dicionario_maneiro.items():
  print(i)

# retorna as chaves
for i in dicionario_maneiro.keys():
  print(i)

# retorna os valores
for i in dicionario_maneiro.values():
  print(i)