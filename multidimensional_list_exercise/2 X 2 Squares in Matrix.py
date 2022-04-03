rows, cols = list(map(int, input().split()))
matrix = []
total = 0
for _ in range(rows):
    a = input().split()
    matrix.append(a)
for i in range(rows - 1, 0, -1):
    for j in range(cols - 1, 0, -1):
        if matrix[i][j] == matrix[i][j - 1] == matrix[i - 1][j] == matrix[i - 1][j - 1]:
            total += 1
print(total)
