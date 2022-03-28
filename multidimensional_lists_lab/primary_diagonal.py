n = int(input())
total = 0
square = []
for i in range(n):
    using = list(map(int, input().split()))
    square.append(using)
    for c in range(i + 1):
        if i == c:
            total += square[i][c]
print(total)
