from collections import deque

quantity_of_the_food = int(input())
sequence_of_integers = deque(map(int, input().split()))
print(max(sequence_of_integers))
condition = False
for i in range(len(sequence_of_integers)):
    order = sequence_of_integers[0]
    if quantity_of_the_food - order >= 0:
        quantity_of_the_food -= sequence_of_integers.popleft()
    else:
        condition = True
        break

if not condition:
    print("Orders complete", end='')
else:
    print("Orders left: ", end='')
    for g in sequence_of_integers:
        print(g, end=" ")
