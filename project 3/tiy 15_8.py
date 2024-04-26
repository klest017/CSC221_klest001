import matplotlib.pyplot as plt
from random import randint

# Produce rolling two D6 dice and make note of results
rolls = 1000
results = [randint(1, 6) * randint(1, 6) for _ in range(rolls)]

# Create graph with results
plt.hist(results, bins=range(1, 37), edgecolor='black', align='left')
plt.xlabel('Product of Two D6 Dice')
plt.ylabel('Frequency')
plt.title('Results of Multiplying Two D6 Dice 1000 Times')
plt.xticks(range(1, 37))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
