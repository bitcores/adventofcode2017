from copy import deepcopy

comps = []
firsts = []

def sumstr(l):
    rstr = 0
    for y in l:
        rstr += y[0] + y[1]
    return rstr

def recuradd(nl, nx):
    global strmax, lenmax
    #print(nl, nx)
    for s in comps:
        #print(s)
        #input()
        if s in nl:
            continue
        if nx in s:
            nnl = deepcopy(nl)
            nnl.append(s)
            nnx = s[0]
            if s[0] == nx:
                nnx = s[1]
            recuradd(nnl, nnx)
            
    nstr = sumstr(nl)
    if nstr > strmax:
        strmax = nstr
    if len(nl) > lenmax[0] or (len(nl) == lenmax[0] and nstr > lenmax[1]):
        lenmax = (len(nl), nstr)
     

with open("input24.txt") as fp:
    for line in fp:
        line = line.strip()
        ends = line.split("/")
        comps.append((int(ends[0]), int(ends[1])))
        if ends[0] == "0" or ends[1] == "0":
            firsts.append((int(ends[0]), int(ends[1])))

#print(comps)
#print(firsts)

strmax = 0
lenmax = (0,0)

for x in firsts:
    nl = []
    nl.append(x)
    nx = x[0]
    if x[0] == 0:
        nx = x[1]

    recuradd(nl, nx)

print("Strength of the strongest bridge:> ", strmax)
print("Strength of the longest bridge:> ", lenmax[1])
    

