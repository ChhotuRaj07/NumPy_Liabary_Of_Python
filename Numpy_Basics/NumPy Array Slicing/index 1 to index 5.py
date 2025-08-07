import numpy as np

Arry = np.array([1,2,3,4,5,6,7,8])
print("Slicing 1 to 5 :",(Arry[1:5]));


# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

# If we don't pass start its considered 0

# If we don't pass end its considered length of array in that dimension

# If we don't pass step its considered 1