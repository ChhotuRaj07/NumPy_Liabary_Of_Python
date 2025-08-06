import numpy as np

Array = np.array([[1,2,3,4,5]
                  ,[5,6,7,8,9]
                  ,[10,11,12,13,14]])

print(Array)
print("Shape:", Array.shape)
print("Data Type:", Array.dtype)


# ✅ 📚 Array & Tensor Shape Cheatmap
# Example	Dimensions (Rank)	Shape	Type
# 5	0-D	()	Scalar
# [1]	1-D	(1,)	Vector
# [1, 2, 3]	1-D	(3,)	Vector
# [[1, 2], [3, 4]]	2-D	(2, 2)	Matrix
# [[1, 2, 3], [4, 5, 6]]	2-D	(2, 3)	Matrix
# [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]	3-D	(2, 2, 2)	3-D Tensor

# 🧠 Manual Shape Finding Rules
# Count outermost brackets → First shape number

# Count inside rows → Second shape number

# Count elements in each row → Third shape number (if nested again)

# Keep going if more levels...

# 🔹 Quick Examples for Practice
# Array	Shape
# [1, 2]	(2,)
# [[2, 4], [6, 8]]	(2, 2)
# [[[1, 2], [3, 4]]]	(1, 2, 2)
# [[[1], [2]], [[3], [4]]]	(2, 2, 1)

# 🧾 Quick Notes
# .shape → Gives shape in code

# Shape is always a tuple: like (3,), (2, 3), etc.

# Shape tells: how many elements in each dimension

# Every NumPy array or tensor has a shape and rank (dimensions)