import numpy as np

vector = np.array([1, 2, 3, 4])

vector_t = vector.transpose()

dot_product_list = []
for a, b in zip(vector, vector_t):
    print(f"{a}+{b}: ",a+b)
    dot_product_list.append(a+b)

sum(dot_product_list)

