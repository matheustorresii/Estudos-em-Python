charlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

arquivo = open("wordlist.txt", "a")

for current in range(4):
  a = [i for i in charlist]
  for x in range(current):
    a = [y + i for i in charlist for y in a]
    for word in a:
      arquivo.write(f'{word}\n') 
arquivo.close()