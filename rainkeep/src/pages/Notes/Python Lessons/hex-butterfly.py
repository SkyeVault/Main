import numpy as np
import matplotlib.pyplot as plt

# Set grid density for detailed hex placement
grid_size = 100  

# Generate a structured hexagonal grid
x = np.tile(np.linspace(-20, 20, grid_size), grid_size)
y = np.repeat(np.linspace(-20, 20, grid_size), grid_size)

# Create an empty array for colors, defaulting to sky blue (background)
colors = np.ones_like(x) * 5  

# Define the butterfly body (black center)
for i in range(len(x)):
    if abs(x[i]) < 1.5 and abs(y[i]) < 10:
        colors[i] = 1  # Black body

# Define more **organic and natural** butterfly wing shapes
for i in range(len(x)):
    # **Upper wings** (larger and curved)
    if (
        (abs(x[i]) > 3 and y[i] > 0) and  
        ((x[i])**2 + (y[i] - 8)**2 < 70)  # Adjusted for smoother curvature
    ):
        colors[i] = np.random.choice([2, 3, 4], p=[0.4, 0.3, 0.3])  # Wing colors: purple, pink, dark blue

    # **Lower wings** (more rounded and curved downward)
    elif (
        (abs(x[i]) > 3 and y[i] < 0) and  
        ((x[i])**2 + (y[i] + 10)**2 < 70)  
    ):
        colors[i] = np.random.choice([2, 3, 4], p=[0.4, 0.3, 0.3])  

# Define a structured color map (black, purple, pink, blue, sky blue)
cmap = plt.cm.colors.ListedColormap(["black", "purple", "hotpink", "darkblue", "skyblue"])

# Create hexbin plot with smooth placement
plt.hexbin(x, y, gridsize=70, C=colors, cmap=cmap, edgecolors='black')

# Add title and remove axes
plt.title("hexbin butterfly")
plt.axis("off")

# Save the figure
plt.savefig("hex_butterfly_final.png", dpi=300)

# Show the plot
plt.show()
