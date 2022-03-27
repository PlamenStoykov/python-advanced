phonebook = {}
while True:
    command = input()
    if command.isdigit():
        num = int(command)
        break
    else:
        name, phone = command.split('-')
        if name not in phonebook:
            phonebook[name] = phone
        phonebook[name] = phone
for i in range(num):
    call_name = input()
    if call_name not in phonebook:
        print(f"Contact {call_name} does not exist.")
    else:
        print(f"{call_name} -> {phonebook[call_name]}")
