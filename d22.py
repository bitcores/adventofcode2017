
partB = True
clgrid = {}
d = 0
# up, right, down, left
mlist = [(-1,0), (0,1), (1,0), (0,-1)]

def chansta(st):
    if partB == True:
        if st == ".":
            return("W")
        if st == "W":
            return("#")
        if st == "#":
            return("F")
        else:
            return(".")
    else:
        if st == ".":
            return("#")
        else:
            return(".")

def chandir(lr):
    global d
    if lr == "l":
        d -= 1
        if d < 0:
            d = 3
    elif lr == "r":
        d += 1
        if d > 3:
            d = 0
    elif lr == "v":
        d += 2
        if d > 3:
            d = d - 4

y = 0
with open("input22.txt") as fp:
    for line in fp:
        clgrid[y] = {}

        line = line.strip()
        for x in range(0, len(line)):
            clgrid[y][x] = line[x]

        y += 1

#print(clgrid)
mid = y // 2
cpos = [mid, mid]

newinfections = 0
for s in range(0, 10000000):
    if cpos[0] not in clgrid:
        clgrid[cpos[0]] = {}
    if cpos[1] not in clgrid[cpos[0]]:
        clgrid[cpos[0]][cpos[1]] = "."

    if clgrid[cpos[0]][cpos[1]] == ".":
        chandir("l")
    elif clgrid[cpos[0]][cpos[1]] == "#":
        chandir("r")
    elif clgrid[cpos[0]][cpos[1]] == "F":
        chandir("v")
    
    clgrid[cpos[0]][cpos[1]] = chansta(clgrid[cpos[0]][cpos[1]])
    if clgrid[cpos[0]][cpos[1]] == "#":
        newinfections += 1
    
    
    cpos[0] = cpos[0] + mlist[d][0]
    cpos[1] = cpos[1] + mlist[d][1]

    #print(cpos)
    #print(clgrid)
    #input()

print("Activities causing new infections:> ", newinfections)