# import matplotlib as plt

# plt.ion()

# x=list(map(int,input().split()))
# y=list(map(int,input().split()))
# x = [1,-1,-1,1,1]
# y = [1,1,-1,-1,1]
# x.append(x[0])
# x.append(x[0])

# plt.plot(x,y)
# plt.show()

import matplotlib.pyplot as plt

import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# The x-axis is the horizontal axis.

# The y-axis is the vertical axis.

xpoints = np.array([1, 8]) 
ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# You can plot as many points as you like, just make sure you have the same number of points in both axis.

xpoints = np.array([5, 7, 12, 17]) 
ypoints = np.array([2, 4, 6, 8 ])
 

# plt.plot(xpoints, ypoints)
# plt.show()


# (Default X-Points) If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 (etc., depending on the length of the y-points.

xpoints = np.array([5, 7, 12, 17]) 
# plt.plot(ypoints)
# plt.show()

# You can use the keyword argument marker to emphasize each point with a specified marker:

plt.plot(ypoints, marker = 'o')
plt.show()



print(plt.__version__)

# two underscore characters are used in __version__.

