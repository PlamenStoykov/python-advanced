from collections import deque

expression = list(input())
using = deque()
counter = 0
condition = False
for i in expression:
    if i == '(':
        using.append(i)
    elif i == '[':
        using.append(i)
    elif i == '{':
        using.append(i)
    elif i in [')', ']', '}']:
        if using:
            if i == ')':
                if using[-1] == '(':
                    using.pop()
            elif i == '}':
                if using[-1] == '{':
                    using.pop()
            elif i == ']':
                if using[-1] == '[':
                    using.pop()
        else:
            using.append(1)
            break
if using:
    print('NO')
else:
    print('YES')
