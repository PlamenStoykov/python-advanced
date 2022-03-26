from collections import deque

green_light = int(input())
free_window = int(input())
command = input()
crossroad_cars = deque()
cars = []
crash = False
while command != 'END':
    if command == 'green':
        crossroad_cars = deque()
    else:
        if len(crossroad_cars) < green_light:  # check green light
            car = deque(command)
            crossroad_cars.extend(car)
            cars.append(command)
            if len(crossroad_cars) > free_window + green_light:  # check crash
                for i in range(len(crossroad_cars) - free_window - green_light - 1):
                    crossroad_cars.pop()
                crash = True
                break

    command = input()
if not crash:
    print("Everyone is safe.")
    print(f"{len(cars)} total cars passed the crossroads.")
else:
    print("A crash happened!")
    print(f"{command} was hit at {crossroad_cars.pop()}.")
