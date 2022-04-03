def doer(integer_row, m, s, rows, cols, bomb):
    if 0 <= rows + integer_row < s:
        for c in range(-1, 2):
            if 0 <= cols + c < s:
                if m[rows + integer_row][cols + c] > 0:
                    m[rows + integer_row][cols + c] -= bomb

        m[rows][cols] = 0
    return m


size = int(input())
matrix = []
for _ in range(size):
    a = list(map(int, input().split()))
    matrix.append(a)
if size:
    b = input()
    while ' ' in b:
        b = b.replace(' ', ',')
    v = list(map(int, b.split(',')))
    for i in range(0, len(v), 2):
        row = v[i]
        col = v[i + 1]
        bomb_value = matrix[row][col]
        matrix = doer(1, matrix, size, row, col, bomb_value)
        matrix = doer(-1, matrix, size, row, col, bomb_value)
        matrix = doer(0, matrix, size, row, col, bomb_value)

alive = [j for i in matrix for j in i if j > 0]
print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")
for i in matrix:
    print(*i)
