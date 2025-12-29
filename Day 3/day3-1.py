with open("Day 3/batteries.txt", "r") as f:
    sequences = f.readlines()

total = 0

for seq in sequences:

    #find maximum number between first digit and second last digit
    first_max = 0
    first_max_index = 0
    for i in range(len(seq)-2):
        if int(seq[i]) > first_max:
            first_max = int(seq[i])
            first_max_index = i

    #find maximum number between found digit and last digit
    second_max = 0
    for j in range(first_max_index + 1, len(seq)-1):
        if int(seq[j]) > second_max:
            second_max = int(seq[j])

    total += ((first_max * 10) + second_max)
    print(total)


