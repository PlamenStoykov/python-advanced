import sys

rows, cols = list(map(int, input().split()))
matrix = []
square = None
total = -sys.maxsize
for _ in range(rows):
    a = list(map(int, input().split()))
    matrix.append(a)
for i in range(rows - 1, 1, -1):
    for j in range(cols - 1, 1, -1):
        using_square = matrix[i][j] + matrix[i][j - 1] + matrix[i][j - 2] + matrix[i - 1][j] + matrix[i - 1][j - 1] + \
                       matrix[i - 1][j - 2] + matrix[i - 2][j] + matrix[i - 2][j - 1] + matrix[i - 2][j - 2]
        if using_square > total:
            total = using_square
            square = tuple(reversed((matrix[i][j], matrix[i][j - 1], matrix[i][j - 2], matrix[i - 1][j], matrix[i - 1][j - 1],
                      matrix[i - 1][j - 2], matrix[i - 2][j], matrix[i - 2][j - 1], matrix[i - 2][j - 2])))
print(f"Sum = {total}")
for c in range(len(square)):
    print(square[c], end=' ')
    if (c + 1) % 3 == 0:
        print()
