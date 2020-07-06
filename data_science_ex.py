import matplotlib.pyplot as plt

arquivo = open("populacao_brasileira.csv")
linhas = arquivo.readlines()

x = [i[6:].strip("\n") for i in linhas]
y = [i[0:4] for i in linhas]

del y[0]
del x[0]

titulo = "Crescimento da População Brasileira 1980-2016"
eixox = "Ano"
eixoy = "População x 100.000.000"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(y, x)
plt.show()