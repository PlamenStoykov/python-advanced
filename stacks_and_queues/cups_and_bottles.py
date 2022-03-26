from collections import deque

wasted_liters = 0

cups_capacity = deque(map(int, input().split()))
bottle_with_water = deque(map(int, input().split()))
while bottle_with_water and cups_capacity:
    cup = cups_capacity.popleft()
    current_bottle = bottle_with_water.pop()
    if cup > current_bottle:
        cup -= current_bottle
        current_bottle = bottle_with_water.pop()
        while True:
            if cup - current_bottle <= 0:
                wasted_liters += current_bottle - cup
                break
            else:
                cup -= current_bottle
                current_bottle = bottle_with_water.pop()

    else:
        wasted_liters += current_bottle - cup
filtered_cups = [str(g) for g in cups_capacity]
filtered_bottles = []
if not bottle_with_water:
    print(f"Cups: {' '.join(filtered_cups)}")
else:
    for g in range(len(bottle_with_water)):
        bottle = str(bottle_with_water.pop())
        filtered_bottles.append(bottle)

    print(f"Bottles: {' '.join(filtered_bottles)}")
print(f"Wasted litters of water: {wasted_liters}")
