
step = 0
pos = 0
#lilen = 5
#inlen = [3,4,1,5]
lilen = 256
inlen = [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]

llist = []

# part 1
for x in range(0, lilen):
    llist.append(x)

for y in inlen:
    sub = []
    spos = pos
    for z in range(0, y):
        if spos > len(llist)-1:
            spos = 0
        sub.append(llist[spos])
        spos += 1

    sub = list(reversed(sub))

    rpos = pos
    for zr in range(0, y):
        if rpos > len(llist)-1:
            rpos = 0
        llist[rpos] = sub[zr]
        rpos += 1

    #print(y, llist, pos)
    #input()

    pos = rpos + step
    if pos > len(llist)-1:
        pos = pos - len(llist)

    step += 1

chksum = llist[0] * llist[1]
print("Result:> ", chksum)


#part 2
#lilen = 5
#instr = "AoC 2017"
lilen = 256
instr = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"

inlen = []
llist = []
step = 0
pos = 0
for x in instr:
    inlen.append(ord(x))
inlen = inlen[:] + [17,31,73,47,23]

#print(inlen)

for x in range(0, lilen):
    llist.append(x)

for p in range(0,64):
    for y in inlen:
        sub = []
        spos = pos
        for z in range(0, y):
            if spos > len(llist)-1:
                spos = 0
            sub.append(llist[spos])
            spos += 1

        sub = list(reversed(sub))

        rpos = pos
        for zr in range(0, y):
            if rpos > len(llist)-1:
                rpos = 0
            llist[rpos] = sub[zr]
            rpos += 1

        #print(y, llist, pos)
        #input()

        pos = rpos + step
        # this took me a bit to find
        while pos > len(llist)-1:
            #print("hitting end")
            pos = pos - len(llist)

        step += 1

#print(llist)

#sparse to dense hash
dhash = ""
for m in range(0,16):
    xord = 0
    for n in range(0,16):
        xord = xord ^ llist[(m*16)+n]
    dhash += '{:02x}'.format(xord)
print("Dense hash:> ", dhash)



