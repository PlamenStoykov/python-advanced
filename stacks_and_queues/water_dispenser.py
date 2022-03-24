from collections import deque

quantity = int(input())
name = input()
queue = deque()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()
while command != 'End':
    if command.startswith('refill'):
        quantity += int(command.split()[-1])
    else:
        litres = int(command)
        name = queue.popleft()
        if litres <= quantity:
            quantity -= litres
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    command = input()
print(f"{quantity} liters left")
