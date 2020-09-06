from copy import deepcopy

usedsquares = 0
lilen = 256
slist = []
#datagrid[y][x]
datagrid = {}
for x in range(0, lilen):
    slist.append(x)

for pp in range(0,128):
    
    #instr = "flqrgnkx-" + str(pp)
    instr = "uugsqrei-" + str(pp)

    datagrid[pp] = {}

    inlen = []
    llist = deepcopy(slist)
    step = 0
    pos = 0
    for x in instr:
        inlen.append(ord(x))
    inlen = inlen[:] + [17,31,73,47,23]

    #print(inlen)

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

    xordlist = []
    binstr = ""
    #sparse to dense hash
    dhash = ""
    for m in range(0,16):
        xord = 0
        tmp = ""
        for n in range(0,16):
            xord = xord ^ llist[(m*16)+n]
        xordlist.append(xord)
        dhash += '{:02x}'.format(xord)
        for z in range(0,8):
            tmp = str(xord % 2) + tmp
            xord = xord >> 1
        binstr += tmp
    #print("Dense hash:> ", dhash)
    #print(xordlist)

    #print(binstr)
    usedsquares += binstr.count("1")
    for x in range(0, len(binstr)):
        if binstr[x] == "1":
            datagrid[pp][x] = 1

print("Used squares:> ", usedsquares)
#print(datagrid)

converts = [(1,0), (-1,0), (0,1), (0,-1)]

def deepsearch(pos, nodlist):
    #print(nodlist)
    #input()
    for c in converts:
        npos = tuple(map(sum, zip(pos, c)))
        #print(npos)
        if npos not in nodlist:
            if npos[0] in datagrid:
                if npos[1] in datagrid[npos[0]]:
                    if datagrid[npos[0]][npos[1]] == 1:
                        nodlist.append((npos[0], npos[1]))
                        nodlist = deepsearch(npos, nodlist)
    return nodlist

regions = 0
for yy in datagrid:
    for xx in datagrid[yy]:
        if datagrid[yy][xx] == 1:
            groupnodes = deepsearch((yy, xx), [(yy, xx)])
            regions += 1
            for u in groupnodes:
                datagrid[u[0]][u[1]] = 0

print("Number of regions:> ", regions)