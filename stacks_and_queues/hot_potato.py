from collections import deque

kids = deque(input().split())
n = int(input())
while len(kids) > 1:
    kids.rotate(-n)
    name = kids.pop()
    print(f"Removed {name}")
print(f"Last is {kids.pop()}")

