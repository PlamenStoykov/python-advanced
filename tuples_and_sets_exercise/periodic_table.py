n = int(input())
table = set()
for i in range(n):
    chemicals = input().split()
    for el in chemicals:
        table.add(el)
for chem in table:
    print(chem)
    