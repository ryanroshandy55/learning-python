# Plotting x and y points
# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
# The function takes parameters for specifying points in the diagram.
    # Parameter 1 is an array containing the points on the x-axis.
    # Parameter 2 is an array containing the points on the y-axis.
# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)

# Without line
xpoints1 = np.array([1, 8])
ypoints1 = np.array([10, 3])
plt.plot(xpoints1, ypoints1, "o")
plt.plot(xpoints1, ypoints1)

# Multiple x and y point
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 10, 1, 10])
plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, "x")

# Default y points
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)

# plt.show()
plt.savefig("fundamentals\\34_matplotlib\\result\\testplotting.png")