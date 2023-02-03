import numpy as np

'''Version 1: The dot product of a vector with itself is the two-norm of that vector, squared.'''

vector = np.array([3, 4])

vector_t = vector.transpose()

dot_product_list = []
for a, b in zip(vector, vector_t):
    print(f"{a}*{b}: ",a*b)
    dot_product_list.append(a*b)

print(sum(dot_product_list))

# 2-norm
# Square root of sums of the squares of entries in vector

square_of_entry = []

for a in vector:
    print(f"{a}^2:",a**2)
    square_of_entry.append(a**2)

print(sum(square_of_entry))


'''Version 2: The dot product of a vector with itself is the two-norm of that vector, squared.'''

u = np.array([3, 4])

dot_product = np.dot(u, u)

# Calculate the two-norm of u using the np.linalg.norm function with ord=2
two_norm = np.linalg.norm(u, ord=2)

print(two_norm)
print(two_norm**2)