rows, cols = [int(i) for i in input().split(', ')]
matrix = []
for r in range(rows):
    using = list(map(int, input().split()))
    matrix.append(using)
for i in range(cols):
    total = 0
    for j in range(rows):
        total += matrix[j][i]
    print(total)
