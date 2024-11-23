import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
ypoints1 = np.array([6,4,10,1])
ypoints2 = np.array([8,2,5,7])

plt.plot(ypoints, marker = "o")
plt.plot(ypoints1, marker = "*")
plt.plot(ypoints2, "o:c")

plt.show()

# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline

# Marker size
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()


# Marker color
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# Set the FACE color to red
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

# Set the color of both the edge and the face to red
ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

# Mark each point with the color named "hotpink":
# https://www.w3schools.com/colors/colors_names.asp
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')