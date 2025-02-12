n = int(input("Enter the size of the square matrix (n x n): "))
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input(f"Enter row {i + 1}: ").split()])
primary_sum = sum(matrix[i][i] for i in range(n))
secondary_sum = sum(matrix[i][n - 1 - i] for i in range(n))
total_sum = primary_sum + secondary_sum
print(f"Primary diagonal sum: {primary_sum}")
print(f"Secondary diagonal sum: {secondary_sum}")
print(f"Total sum of both diagonals: {total_sum}")