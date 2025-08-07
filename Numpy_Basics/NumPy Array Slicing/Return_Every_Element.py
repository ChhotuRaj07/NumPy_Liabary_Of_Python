import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# array[start : stop : step]

print("The Return Every Element",(arr[1:5:2] ))

# Start at index 1 → 2

# Stop before index 5 → don't include 6

# Step by 2

# So:

# Index 1 → 2

# Index 3 → 4

# ✅ Output: [2 4]