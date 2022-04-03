def sum_ascii(nick, num):
    total = 0
    for letter in nick:
        total += ord(letter)

    return total // num


odd = set()
even = set()
n = int(input())
for i in range(1, n + 1):
    name = input()
    result = sum_ascii(name, i)
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

if sum(odd) == sum(even):
    using = odd | even
    e = [str(i) for i in using]
    print(', '.join(e))

elif sum(odd) > sum(even):
    using = odd - even
    e = [str(i) for i in using]
    print(', '.join(e))
elif sum(even) > sum(odd):
    using = even.symmetric_difference(odd)
    e = [str(i) for i in using]
    print(', '.join(e))
