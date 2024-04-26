import matplotlib.pyplot as plt
from random import randint

# Simulate rolling two eight-sided dice 1000 times
rolls = 1000
results = [randint(1, 8) + randint(1, 8) for _ in range(rolls)]

# Visualize the results
plt.hist(results, bins=range(2, 17), edgecolor='black', align='left')
plt.xlabel('Sum of Two Dice')
plt.ylabel('Frequency')
plt.title('Results of Rolling Two Eight-Sided Dice 1000 Times')
plt.xticks(range(2, 17))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
