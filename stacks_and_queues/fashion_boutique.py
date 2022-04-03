from collections import deque

clothes = deque(map(int, input().split()))
capacity = int(input())
total_racks = 1

using = 0
while clothes:
    current_cloth = clothes.pop()
    if current_cloth + using <= capacity:
        using += current_cloth
    else:
        total_racks += 1
        using = current_cloth
print(total_racks)

