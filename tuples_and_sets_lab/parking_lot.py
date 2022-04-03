n = int(input())
parking = set()
for i in range(n):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        parking.add(car_number)
    elif direction == 'OUT':
        parking.discard(car_number)
if parking:
    for c in parking:
        print(c)
else:
    print('Parking Lot is Empty')
