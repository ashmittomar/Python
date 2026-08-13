import numpy as np

# Take matrix size
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# Enter first matrix
print("Enter first matrix:")
matrix1 = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

matrix1 = np.array(matrix1)

# Enter second matrix
print("Enter second matrix:")
matrix2 = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

matrix2 = np.array(matrix2)

# Display matrices
print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Operations
print("\nAddition:")
print(matrix1 + matrix2)

print("\nSubtraction:")
print(matrix1 - matrix2)

print("\nElement-wise Multiplication:")
print(matrix1 * matrix2)

print("\nTranspose of Matrix 1:")
print(matrix1.T)

print("\nTranspose of Matrix 2:")
print(matrix2.T)