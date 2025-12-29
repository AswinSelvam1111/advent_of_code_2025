start = 50
counter = 0

with open("Day 1/sequence.txt", "r") as f:
    sequences = f.readlines()

for seq in sequences:
    
    if seq[0] == "R":
        start = start + int(seq.strip("R"))
    elif seq[0] == "L":
        start = start - int(seq.strip("L"))

    start = start % 100
    #modulus works with negative numbers as well!!

    if start == 0:
        counter += 1
        
print(counter)

