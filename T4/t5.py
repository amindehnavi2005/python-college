import numpy as np

def read_matrix(name, m, n):
    print(f"Enter elements of matrix {name} (row by row):")
    elements = []
    for i in range(m):
        row = []
        for j in range(n):
            val = int(input(f"{name}[{i}][{j}]: "))
            row.append(val)
        elements.append(row)
    return np.array(elements)

def sum_matrices(A, B):
    return A + B

# ---- گرفتن ورودی ----
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

A = read_matrix('A', m, n)
B = read_matrix('B', m, n)

C = sum_matrices(A, B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nSum of A and B:")
print(C)
