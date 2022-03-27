input_line = list(input())
other = set(input_line)
using = list(other)
using.sort()
for i in using:
    print(f"{i}: {input_line.count(i)} time/s")




