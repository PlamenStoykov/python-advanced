nums = tuple(input().split())
nums_dict = {}
for i in nums:
    if i not in nums_dict:
        nums_dict[i] = 1
    else:
        nums_dict[i] += 1
for g in nums_dict:
    c = float(g)
    print(f"{c} - {nums_dict[g]} times")


