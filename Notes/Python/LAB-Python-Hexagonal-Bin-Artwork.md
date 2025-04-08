# **Lab: Creating Hexagonal Chart Artwork with Pandas & Matplotlib**

## **Introduction**
This lab will teach you how to use **Python, Pandas, and Matplotlib** to generate **hexagonal bin charts** as a form of **data-driven artwork**. The goal is to create a structured **hex grid**, adjust values, and use **color gradients** to make unique visuals—similar to **pixel art but using hexagons**.

---

## **Lab Objectives**
By the end of this lab, you will:
✅ **Create a hexagonal grid** using Matplotlib.  
✅ **Determine grid values** for artistic data representation.  
✅ **Apply conditional color mapping** for artistic effects.  
✅ **Customize grid density and placement** for meaningful compositions.  

---

## **1. Prerequisites**
Before starting, make sure you have Python installed. You will also need:
- **Pandas** – For data manipulation.
- **Matplotlib** – For visualization.
- **NumPy** – To generate data points.

Install them using:
```sh
pip install pandas matplotlib numpy
```

---

## **2. Generating a Hexagonal Grid**
A **hexagonal bin plot** groups points into **hexagonal cells**, making it ideal for structured artwork.

### **Step 1: Import Libraries**
```python
import numpy as np
import matplotlib.pyplot as plt
```

### **Step 2: Generate Data Points**
```python
# Create random x, y points
x = np.random.randn(10000)
y = np.random.randn(10000)
```

### **Step 3: Create a Basic Hexbin Chart**
```python
plt.hexbin(x, y, gridsize=40, cmap='inferno', edgecolors='none')
plt.title("Hexagonal Art - Basic Chart")
plt.axis("off")  # Hide axes for a clean look
plt.show()
```

✅ You should now see a **basic hexagonal plot** with an inferno colormap.

---

## **3. Adjusting Values for Artistic Control**

Now, let’s control the **grid density** and **value distribution**.

### **Step 4: Modify the Grid Size**
```python
plt.hexbin(x, y, gridsize=60, cmap='plasma', edgecolors='white')
plt.title("Hexagonal Art - Adjusted Grid")
plt.axis("off")
plt.show()
```
✅ **Increasing `gridsize` makes smaller hexagons, allowing for more detail.**

---

## **4. Customizing Colors and Patterns**

We can map values to **specific colors** using conditions.

### **Step 5: Apply Conditional Color Mapping**
```python
# Generate color values based on density
color_map = plt.cm.get_cmap("viridis")
plt.hexbin(x, y, gridsize=50, cmap=color_map, mincnt=1)
plt.title("Hexagonal Art - Color Mapping")
plt.axis("off")
plt.show()
```
✅ Now, **hexagons with more data points will appear in a different color**, creating an artistic pattern.

---

## **5. Creating Structured Designs**
To create intentional artwork, we can **define our own structured grid** instead of using random points.

### **Step 6: Creating a Custom Grid for Artistic Placement**
```python
# Define structured hexagon positions manually
x_custom = np.tile(np.arange(-10, 10, 0.5), 10)
y_custom = np.repeat(np.arange(-10, 10, 0.5), 10)

plt.hexbin(x_custom, y_custom, gridsize=30, cmap='coolwarm', edgecolors='black')
plt.title("Hexagonal Art - Structured Grid")
plt.axis("off")
plt.show()
```
✅ Now, you have a **controlled pattern** rather than random placement.

---

## **6. Adding Artistic Elements**
To make our hex art more like **a honeycomb with a bee**, we can overlay images or shape cutouts.

### **Step 7: Overlay a Bee Image (Optional)**
```python
import matplotlib.image as mpimg

# Load an image of a bee
img = mpimg.imread("bee.png")

fig, ax = plt.subplots()
ax.imshow(img, extent=[-5, 5, -5, 5], alpha=0.5)  # Overlay with transparency
plt.hexbin(x_custom, y_custom, gridsize=30, cmap='cividis', edgecolors='black')
plt.title("Hexagonal Art - Bee in Honeycomb")
plt.axis("off")
plt.show()
```
✅ This will **overlay a bee image** on top of the hex chart to blend data and artwork.

---

## **7. Summary & Next Steps**
| **Concept** | **What We Learned** |
|------------|------------------|
| **Hexagonal Binning** | Creating structured hex grids |
| **Data & Grid Values** | Controlling placement for artistic control |
| **Color Mapping** | Assigning colors based on values |
| **Custom Patterns** | Placing hexagons intentionally |
| **Overlaying Images** | Blending visuals with charts |

### **What’s Next?**
✅ **Experiment with different colormaps (`cmap`) for creative effects.**  
✅ **Try different grid sizes (`gridsize`) for various levels of detail.**  
✅ **Use real-world data (like city heat maps) instead of random values.**  
✅ **Generate designs that resemble flowers, abstract shapes, or structured patterns.**  

🚀 **Hexagonal bin art is a fusion of data visualization and creative expression—keep exploring!**

