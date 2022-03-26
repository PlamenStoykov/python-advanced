from collections import deque

n = int(input())
col = deque()
for i in range(n):
    query = input()
    if query.startswith('1'):
        element = int(query.split()[1])
        col.append(element)
    elif query == '2':
        if col:
            col.pop()
    elif query == '3':
        if col:
            print(max(col))
    elif query == '4':
        if col:
            print(min(col))
while col:
    if len(col) != 1:
        print(col.pop(), end=', ')
    else:
        print(col.pop())
