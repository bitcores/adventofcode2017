from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

ptcl = {}
ptclcnt = {}

# part B - set True
collisions = False

if rank == 0:    
    no = 0

    with open("input20.txt") as fp:
        for line in fp:
            line = line.strip()
            pva = line.split(", ")
            
            ptcl[no] = {}
            ptclcnt[no] = 0

            man = 0
            ptcl[no]["p"] = []
            for x in pva[0][3:-1].split(","):
                ptcl[no]["p"].append(int(x))
                man += abs(int(x))
            
            ptcl[no]["v"] = []
            for x in pva[1][3:-1].split(","):
                ptcl[no]["v"].append(int(x))
            
            ptcl[no]["a"] = []
            for x in pva[2][3:-1].split(","):
                ptcl[no]["a"].append(int(x))
            
            ptcl[no]["man"] = man

            no += 1

ptcl = comm.bcast(ptcl, 0)
closest = 0
#print(ptcl)

for p in range(0, 1000):
    if rank == 0:
        dsize = len(ptcl) // size
        mplist = []
        pkeys = list(ptcl.keys())

        for p in range(0, size):
            spdict = {}
            for d in range(p*dsize, p*dsize+dsize):
                spdict[pkeys[d]] = ptcl[pkeys[d]]
            mplist.append(spdict)
    else:
        mplist = None
    
    sptcl = comm.scatter(mplist, 0)

    # check for an remove collisions
    if collisions:
        cols = set()
        for c in sptcl.keys():
            for y in ptcl.keys(): 
                if c == y or c in cols:
                    continue

                if ptcl[c]["p"] == ptcl[y]["p"]:
                    cols.add(c)
                    cols.add(y)

        cols = comm.gather(cols, 0)

    if rank == 0:
        mind = 9999999
        x = 0
        c = 0  
        
        if collisions:
            for g in cols:
                for r in g:
                    ptcl.pop(r)           

        for x in ptcl.keys():
            for y in range(0,3):
                ptcl[x]["v"][y] += ptcl[x]["a"][y]

            man = 0
            for z in range(0,3):
                ptcl[x]["p"][z] += ptcl[x]["v"][z]
                man += abs(ptcl[x]["p"][z])
            
            ptcl[x]["man"] = man

            if man < mind:
                mind = man
                closest = x
            
            x += 1

        ptclcnt[closest] += 1

    ptcl = comm.bcast(ptcl, 0)
        
        #print(ptcl)
        #print("closest:> ", closest)
        #input("looped")

if rank == 0:
    m = max(ptclcnt, key=ptclcnt.get)
    print("Particle most often close to 0:> ", m, ptclcnt[m])
    if collisions:
        print("Len:>", len(ptcl))
