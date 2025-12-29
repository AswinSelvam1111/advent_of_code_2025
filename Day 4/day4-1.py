#the core problem: for each paper check its surrounding 8 papers
#if less than 4 papers, then increment to total
#note: x is row, y is column

with open("Day 4/paper.txt", "r") as f:
    sequences = f.readlines()

big_total = 0


#to check if the position is valid from its 8 surrounding positions
def check_position(x,y):
    total = 0
    if check(x-1,y-1):
        total += 1
    if check(x-1,y):
        total += 1
    if check(x-1,y+1):
        total += 1
    if check(x,y-1):
        total += 1
    if check(x,y+1):
        total += 1
    if check(x+1,y-1):
        total += 1
    if check(x+1,y):
        total += 1
    if check(x+1,y+1):
        total += 1  
    if total < 4:
        return True
    else:
        return False

#to check if it is counted as a paper
def check(x,y):
    if ((x < 0) or (x > 139) or (y < 0) or (y > 139)):
        return False
    elif sequences[x][y] == ".":
        return False
    else:
        return True
