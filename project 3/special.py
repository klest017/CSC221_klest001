import matplotlib.pyplot as plt

# Years for which we have population data
years = [2000, 2005, 2010, 2015, 2020]

# Population data for New York for each year
population = [8008278, 8175133, 8175133, 8537673, 8820222]  # Example data (fictional)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(years, population, marker='o', linestyle='-')

# Adding labels and title
plt.title('Population Growth of New York')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)

# Adding annotations for each data point
for i in range(len(years)):
    plt.annotate(population[i], (years[i], population[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Displaying the plot
plt.tight_layout()
plt.show()
