def range_splitter(ranges):
    result = ranges.split(',')
    num_one = int(result[0])
    num_two = int(result[1])
    using = set()
    for d in range(num_one, num_two + 1):
        using.add(d)
    return using


def intersection(a, b):
    r = a & b
    return r


n = int(input())
length = 0
for i in range(n):
    range_one, range_two = input().split('-')
    first = range_splitter(range_one)
    second = range_splitter(range_two)
    function_return = intersection(first, second)
    if len(function_return) > length:
        longest = function_return
        length = len(longest)
longest = list(longest)
print(f"Longest intersection is {longest} with length {length}")
