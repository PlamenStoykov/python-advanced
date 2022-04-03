import re

ready = []
n = int(input())
pattern = r'!([A-Z][a-z]{3,})!:\[([a-zA-Z]{8,})\]'
for i in range(n):
    condition = False
    message = input()
    result = re.finditer(pattern, message)
    for c in result:
        command = c.group(1)
        using = c.group(2)
        if using:
            condition = True
    if not condition:
        print('The message is invalid')
    else:
        for letter in using:
            ready.append(ord(letter))
        print(f"{command}:", end=" ")
        counter = 0
        for num in ready:
            if counter == len(ready) -1:
                print(num)
            else:
                print(num, end=" ")
            counter += 1