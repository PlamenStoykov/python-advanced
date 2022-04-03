exercise = input()
parentheses = []
for i in range(len(exercise)):
    el = exercise[i]
    if el == '(':
        parentheses.append(i)
    elif el == ')':
        start_index = parentheses.pop()
        print(exercise[start_index: i + 1])

