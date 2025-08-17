import numpy as np
# Make a view, change the original array, and display both arrays:

arr = np.array([1, 2, 3, 4, 5])

x = arr.view()

arr[0] = 42
print(arr)
print(x)