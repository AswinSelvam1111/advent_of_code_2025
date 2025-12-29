with open("Day 3/batteries.txt", "r") as f:
    sequences = f.readlines()

#need a total
big_total = 0

for seq in sequences:
    seq = seq.strip()

    #need a array for index
    index_array = [0]
    total = 0

    for i in range(0, 12):

        max = 0
        max_index = 0
        for j in range(index_array[i], len(seq) - 11 + i):
            if int(seq[j]) > max:
                max = int(seq[j])
                max_index = j

        total += (max * (10 ** (11 - i)))
        index_array.append(max_index + 1)
    
    print("Partial total:", total)
    big_total += total

print(big_total)
