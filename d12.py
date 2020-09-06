
programs = {}

with open("input12.txt") as fp:
    for line in fp:
        pset = line.strip().split(" <-> ")
        subp = pset[1].split(", ")
        for x in range(0, len(subp)):
            subp[x] = int(subp[x])
        
        programs[int(pset[0])] = subp


# count programs connected to program 0
g = 0
gs = set()
gs.add(0)

def regur(l, s):
    for n in programs[l]:
        if n not in s:
            s.add(n)
            regur(n, s)
    return s

gs = regur(g, gs)
#print(gs)
print("Number of programs in group 0:> ", len(gs))

groups = []
groups.append(gs)

for x in programs:
    if x == 0:
        continue
    
    found = False
    for p in groups:
        if x in p:
            found = True

    if not found:
        ns = set()
        ns.add(x)
        ns = regur(x, ns)
        groups.append(ns)

print("Number of program groups:> ", len(groups))
    
