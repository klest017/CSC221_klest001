import matplotlib.pyplot as plt
import numpy as np

# Create the first 5000 cubic numbers
first_5000_cubic = [x**3 for x in range(1, 5001)]

# Generate x values for the plot
x_values = np.arange(1, 5001)

# Plot the first 5000 cubic numbers with a colormap
plt.figure(figsize=(10, 6))
plt.scatter(x_values, first_5000_cubic, c=first_5000_cubic, cmap='viridis', s=8, alpha=0.6)
plt.colorbar(label='Cubic Value')
plt.title('First 5000 Cubic Numbers with Colormap')
plt.xlabel('Index')
plt.ylabel('Cubic Value')
plt.grid(True)

# Show the plot
plt.show()
