n = int(input())
all_guests = set()
visiting = set()
for i in range(n):
    code = input()
    all_guests.add(code)
guests_code = input()
while guests_code != 'END':
    visiting.add(guests_code)
    guests_code = input()
diff = all_guests.difference(visiting)
print(len(diff))
result = sorted(diff)
for i in result:
    print(i)




