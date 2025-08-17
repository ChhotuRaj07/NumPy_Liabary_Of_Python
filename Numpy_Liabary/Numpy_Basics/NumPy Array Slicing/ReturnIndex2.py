import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("From both elements, return index 2:",arr[ 0:2 , 2])

# What is arr[0:2, 2] doing?
# Format: arr[row_start:row_stop, column_index]

# 0:2 → means from row 0 to row 1 (2 is excluded, as always in Python).

# 2 → means column index 2 (the 3rd column, since indexing starts at 0)


# Let’s visualize:

# Row	Index 0	Index 1	Index 2	Index 3	Index 4
# 0	1	2	3	4	5
# 1	6	7	8	9	10

# So:

# From row 0 → column 2 = 3

# From row 1 → column 2 = 8

# 🟩 Final result: [3 8]

