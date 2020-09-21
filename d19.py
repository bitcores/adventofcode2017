from copy import deepcopy
grid = {}
y = 0

with open("input19.txt") as fp:
    for line in fp:
        grid[y] = {}
        for x in range(0, len(line)-1):
            if line[x] != " ":
                grid[y][x] = line[x]
        y += 1

# direction
# 0 = down
# 2 = up
# 1 = left
# 3 = right
d = 0
md = { 0: [1, 0], 2: [-1, 0], 1: [0, -1], 3: [0, 1] }

# grid[0] should contain only one value which is the start point
# and the initial direction is downward
if len(grid[0]) != 1:
    print("Invalid grid")
    exit()

chkp = ""
scnt = 0
end = False
# pos is a [y, x] list
pos = [0, list(grid[0].keys())[0]]

while not end:
    #print(pos)
    npos = deepcopy(pos)
    npos[0] += md[d][0]
    npos[1] += md[d][1]
    scnt += 1

    if npos[0] not in grid or npos[1] not in grid[npos[0]]:
        #print("No continue")
        break

    elif grid[npos[0]][npos[1]] == "+":
        pos = deepcopy(npos)
        for c in list(md.keys()):
            if c % 2 == d % 2:
                continue
            npos = deepcopy(pos)
            npos[0] += md[c][0]
            npos[1] += md[c][1]

            if npos[0] in grid and npos[1] in grid[npos[0]]:
                d = c
                break
        continue
            
    elif grid[npos[0]][npos[1]] == "-" or grid[npos[0]][npos[1]] == "|":
        pos = deepcopy(npos)
        continue
    
    else:
        chkp += grid[npos[0]][npos[1]]
        pos = deepcopy(npos)
        continue

print("Letters collected:> ", chkp)
print("Step count:> ", scnt)
