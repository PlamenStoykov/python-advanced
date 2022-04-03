def avg_grade(a):
    return sum(a) / len(a)

n = int(input())
students_shkolo = {}
for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in students_shkolo:
        students_shkolo[name] = []
    students_shkolo[name].append(grade)
for k, v in students_shkolo.items():
    average = avg_grade(v)
    r = [str(f'{i:.2f}')for i in v]
    o = ' '.join(r)

    print(f"{k} -> {o} (avg: {average:.2f})")

