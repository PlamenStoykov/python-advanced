lines = input()
my_dict = {}
while lines != 'Log out':
    tokens = lines.split(': ')
    command = tokens[0]
    username = tokens[1]
    if command == 'New follower':
        if username not in my_dict:
            my_dict[username] = [0, 0]

    elif command == 'Like':
        count = int(tokens[2])
        if username not in my_dict:
            my_dict[username] = [count, 0]
        else:
            my_dict[username][0] += count
    elif command == 'Comment':
        if username not in my_dict:
            my_dict[username] = [1, 0]
        else:
            my_dict[username][1] += 1
    elif command == 'Blocked':
        if username not in my_dict:
            print(f"{username} doesn't exist.")
        else:
            my_dict.pop(username)

    lines = input()
print(f"{len(my_dict)} followers")
for key, value in my_dict.items():
    print(f"{key}: {sum(value)}")
