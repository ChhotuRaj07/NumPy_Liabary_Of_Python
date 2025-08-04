

# ndim, which tells you the number of dimensions (a.k.a. rank) of each array.
import numpy as np

a = np.array(42)                       # Scalar
b = np.array([1, 2, 3, 4, 5])          # 1-D Array (Vector)
c = np.array([[1, 2, 3], [4, 5, 6]])   # 2-D Array (Matrix)
d = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])  # 3-D Tensor

print(a.ndim)  # ➝ 0
print(b.ndim)  # ➝ 1
print(c.ndim)  # ➝ 2
print(d.ndim)  # ➝ 3
