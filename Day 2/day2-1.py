import re

with open("Day 2/ranges.txt", "r") as f:
    range_list = f.readlines()

ranges = re.split("[,]", range_list[0])
total = 0

for ranger in ranges:
    bounds = re.split("[-]", ranger)
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])

    for num in range(lower_bound, upper_bound + 1):
        if len(str(num)) % 2 == 0:
            first_half = str(num)[:len(str(num))//2]
            second_half = str(num)[len(str(num))//2:]
            if first_half == second_half:
                total += num
        
print(total)