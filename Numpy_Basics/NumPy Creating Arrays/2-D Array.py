import numpy as np

# Creating a 2-D array with two arrays as rows
# These are often used to represent matrix or 2nd order tensors.

# 🔷 What is a Tensor?
# A tensor is a mathematical object that generalizes the concepts of scalars, vectors, and matrices to higher dimensions. It’s like a multi-dimensional array.

# 🔢 Tensor Breakdown by Dimensions (or “Order” or “Rank”):
# Tensor Type	Order	Example	Description
# Scalar	0	5	A single number (0-D)
# Vector	1	[1, 2, 3]	A list of numbers (1-D)
# Matrix	2	[[1, 2], [3, 4]]	2D table of numbers
# 3D Tensor	3	[[[1, 2], [3, 4]], ...]	A list of matrices
# n-D Tensor	n	n-dimensional array	Beyond 3D, e.g., images/video

# 🧠 In Simple Words:
# Think of a tensor as just a container for data with any number of dimensions.

# In machine learning (like TensorFlow or PyTorch), tensors are used to store and process data such as:

# Images (3D tensors: height × width × color channels)

# Videos (4D tensors: frames × height × width × channels)

# Text sequences, etc.


Array = np.array([[1,5,2,3,4,5], [5,4,2,3,4,6]])

print(Array)