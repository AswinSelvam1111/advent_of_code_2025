start = 50
counter = 0

with open("Day 1/sequence.txt", "r") as f:
    sequences = f.readlines()

#print(len(sequences))
for seq in sequences:

    if seq[0] == "R":
        sequence = int(seq[1:])
        for i in range(sequence):
            start = (start + 1) % 100
            if start == 0:
                counter += 1

    elif seq[0] == "L":
        sequence = int(seq[1:])
        for i in range(sequence):
            start = (start - 1) % 100
            if start == 0:
                counter += 1
                
print(counter)