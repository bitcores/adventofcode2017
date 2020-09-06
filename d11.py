
#inp = "ne,ne,ne"

f = open("input11.txt")
inp = f.readline()
f.close()

steps = inp.split(",")

# (y, x)
start = (0,0)

gdist = 0

pos = start
for x in steps:
    if x == "nw":
        pos = (pos[0]+1, pos[1]-1)
    elif x == "n":
        pos = (pos[0]+2, pos[1])
    elif x == "ne":
        pos = (pos[0]+1, pos[1]+1)
    elif x == "sw":
        pos = (pos[0]-1, pos[1]-1)
    elif x == "s":
        pos = (pos[0]-2, pos[1])
    elif x == "se":
        pos = (pos[0]-1, pos[1]+1)

    y = abs(pos[0])
    z = abs(pos[1])

    xsteps = 0
    if y > z:
        dif = y - z
        xsteps = (dif/2) + z
    else:
        dif = z - y
        xsteps = (dif/2) + y
    if xsteps > gdist:
        gdist = xsteps
    
#print(pos)
y = abs(pos[0])
z = abs(pos[1])

xsteps = 0
if y > z:
    dif = y - z
    xsteps = (dif/2) + z
else:
    dif = z - y
    xsteps = (dif/2) + y

print("Distance at end:> ", xsteps)
print("Greatest distance:> ", gdist)