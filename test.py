# Original tuple
original_tuple = (1, 2, 3, 4, 5)

# Index of the element to be changed
index_to_change = 2

# New value for the element
new_value = 10

# Create a new tuple with the desired element changed
new_tuple = original_tuple[:index_to_change] + (new_value,) + original_tuple[index_to_change+1:]

print("Original tuple:", original_tuple)
print("New tuple:", new_tuple)