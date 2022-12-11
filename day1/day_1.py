print('hello again!')

# with open('day_1_input.txt') as f:
#     lines = f.readlines()
#     global_max = 0
#     local_max = 0
#     for line in lines:
#         if line == '\n':
#             global_max = max([global_max, local_max])
#             local_max=0
#         else:
#             local_max += int(line)
#     print('the answer is:',max([global_max, local_max]))

with open('day_1_input.txt') as f:
    lines = f.readlines()
    totals = []
    total = 0
    for line in lines:
        if line == '\n':
            totals.append(total)
            total=0
        else:
            total += int(line)
    totals.sort()
    print(sum(totals[-3:]))