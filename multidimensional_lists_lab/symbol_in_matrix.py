n = int(input())
matrix = []
condition = False
for i in range(n):
    chars = list(input())
    matrix.append(chars)
search = input()

for g in range(n):
    for c in range(n):
        if matrix[g][c] == search:
            condition = True
            print(f"({g}, {c})")
            break
        if condition:
            break
if not condition:
    print(f"{search} does not occur in the matrix")
