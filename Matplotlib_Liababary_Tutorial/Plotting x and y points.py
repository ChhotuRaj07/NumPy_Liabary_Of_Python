import matplotlib.pyplot as plt
import numpy as np


# Parameter 2 is an array containing the points on the y-axis.
# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

# X_axis = np.array([1,8])
# Y_axis = np.array([3,10])
# plt.plot(X_axis,Y_axis)
# plt.show()

# ---------------------------------------------

# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.


# X_axis = np.array([1,8])
# Y_axis = np.array([3,10])
# plt.plot(X_axis,Y_axis,'o')
# plt.show()



# -----------------------------------------------------------------
# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

# X_points = np.array([1,2,6,8])
# Y_points =  np.array([3,8,1,10])

# plt.plot(X_points,Y_points)
# plt.show()


# ----------------------------------------------------------------------------

# Default X-Points

# Plotting without x-points:

Y_axis = np.array([3, 8, 1, 10, 5, 7])
plt.plot(Y_axis)
plt.show()