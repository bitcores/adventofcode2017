
fwb = {}
lst = 0

with open("input13.txt") as fp:
    for line in fp:
        ns = line.strip().split(": ")
        fwb[int(ns[0])] = int(ns[1])
        lst = int(ns[0])

#print(fwb)


sev = 0

for x in range(0, lst+1):
    if x in fwb.keys():
        if x % ((fwb[x]-1)*2) == 0:
            #print(x, (fwb[x]-1)*2)
            sev += x * fwb[x]

print("0 delay severity:> ", sev)

delay = 0

loop = True
while loop:
    loop = False
    delay += 1
    for x in range(0, lst+1):
        if x in fwb.keys():
            if (x+delay) % ((fwb[x]-1)*2) == 0:
                loop = True
                break

print("Delay to pass through safely:> ", delay)

