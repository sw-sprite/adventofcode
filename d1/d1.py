with open("input.txt") as f:
    lines = []
    for line in f:
        lines.append(line) 

# print(lines)

cur_sum = 0; elf_max = 0; cal_arr = []
for i in lines:
    # print(i)
    if i != '\n':
        cur_sum = cur_sum + int(i[:-1])
        # print(int(i[:-1]))
    else:
        # print('skipped')
        cal_arr.append(cur_sum)
        elf_max = max(elf_max, cur_sum)
        cur_sum = 0

cal_arr.sort()

print(elf_max)
print(sum(cal_arr[-3:]))