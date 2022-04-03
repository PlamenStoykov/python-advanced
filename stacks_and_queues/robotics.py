robots = input().split(';')
robots_and_time = [i.split('-')for i in robots]
print(robots_and_time)
starting_time = input().split()
command = input()
seconds = 0
while command != 'End':
    seconds += 1

    command = input()

