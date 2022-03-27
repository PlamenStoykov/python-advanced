input_line = input().split()
n = int(input_line[0])
m = int(input_line[1])
first_set = set()
second_set = set()
for i in range(m + n):
    num = input()
    if i < n:
        first_set.add(num)
    else:
        second_set.add(num)
result = first_set & second_set
for i in result:
    print(i)
