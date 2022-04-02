def checker(r, c, b, row, col):
    positions = []
    if r + 1 < row:
        positions.append((r+1, c + 2))
        p


        


rows, cols = list(map(int, input().split()))
matrix = []
total = 0
for _ in range(rows):
    a = list(input())
    matrix.append(a)
for i in range(rows - 1, 1, -1):
    for j in range(cols - 1, 1, -1):
        if matrix[i][j] == 'K':
            pass
