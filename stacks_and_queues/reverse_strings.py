input_line = list(input())
words_list = []
while input_line:
    words_list.append(input_line.pop())

print(''.join(words_list))
