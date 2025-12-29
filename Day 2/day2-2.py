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
        L = len(str(num))

        for digits in range(2, L + 1):
            if L % digits == 0:
                length = L // digits
                segments = [str(num)[i * length : (i + 1) * length] for i in range(digits)]
                if all(segment == segments[0] for segment in segments):
                    total += num
                    break

print(total)