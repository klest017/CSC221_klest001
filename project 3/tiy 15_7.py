import matplotlib.pyplot as plt
from random import randint

# Simulate rolling three D6 dice and make note results

rolls = 1000
results = [randint(1, 6) + randint(1, 6) + randint(1, 6) for _ in range(rolls)]

# Create graph with results
plt.hist(results, bins=range(3, 19), edgecolor='black', align='left')
plt.xlabel('Sum of Three D6 Dice')
plt.ylabel('Frequency')
plt.title('Results of Rolling Three D6 Dice 1000 Time')
plt.xticks(range(3, 19))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
