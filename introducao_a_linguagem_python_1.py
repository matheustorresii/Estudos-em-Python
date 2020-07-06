# exponencial
print(2 ** 3)

# let i = 10; i < 20; i+2
# for i in range(10,20,2):
  # print(i)

nome = "Torres"

nome = nome + " "

# remove caracteres especiais/a mais
nome.strip()

# conta caracteres
tamanho = len(nome)
print(tamanho)

# minusculo/maiusculo
print(nome.lower())
print(nome.upper())

string_foda = "O rato roeu a roupa do rei de roma"

# divide a string em array
array_foda = string_foda.split(" ")

# modicia a string
string_foda = string_foda.replace("o rei", "a rainha")

print(array_foda)

# busca o index da palavra, caso n acha, retorna -1
busca = string_foda.find("rei")
print(busca)