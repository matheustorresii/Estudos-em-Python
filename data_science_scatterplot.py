import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 6, 1, 0]
s = [200, 25, 400, 3300, 100]

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="#c1c3c1", linestyle="-.")
plt.scatter(x, y, label="Pontos", color="#e1a910", marker="^", s=s)

plt.legend()

# plt.show()
plt.savefig("fig.png", dpi=300)