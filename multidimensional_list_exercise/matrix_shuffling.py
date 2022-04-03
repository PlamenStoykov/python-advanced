def checker(r1, c1, r2, c2, r, c):
    if min(r1, r2) >= 0 and max(r1, r2) < r:
        if min(c1, c2) >= 0 and max(c1, c2) < c:
            return True
    else:
        return False


rows, cols = list(map(int, input().split()))
matrix = []
for _ in range(rows):
    a = input().split()
    matrix.append(a)
command = input()
while command != 'END':
    tokens = command.split()
    if tokens[0] == 'swap' and len(tokens) == 5:
        command = command.replace('swap', '')
        row1, col1, row2, col2 = list(map(int, command.split()))
        if checker(row1, col1, row2, col2, rows, cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for i in matrix:
                print(*i)
        else:
            print('Invalid input!')

    else:
        print('Invalid input!')
    command = input()
