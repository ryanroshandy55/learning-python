import matplotlib.pyplot as plt
import numpy as np
import image

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
# plt.show()
plt.savefig('fundamentals\\33_matplotlib\\result\\testplot.png')
plt.savefig('fundamentals\\33_matplotlib\\result\\testplot.jpg')