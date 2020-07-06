import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
  random_number = random.randint(0, 100)
  vetor.append(random_number)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()