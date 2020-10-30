from mpi4py import MPI
from copy import deepcopy
from math import sqrt
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

# processing the block looking for matches
# z: pass, r: rotate, h: flip h, v: flip v
pro = ["z", "r", "h", "v", "r", "h", "v", "r", "r"]

def joinery(xlist,c=True):
    out = ""
    for y in xlist:
        for x in xlist[y]:
            out += xlist[y][x]
        out += "/"
    if c:
        return out[:-1]
    else:
        return out

def rotater(zdict):
    ndict = deepcopy(zdict)
    l = len(zdict[0]) - 1
    d = 0
    for y in zdict:
        c = l
        for x in zdict[y]:
            ndict[c][d] = zdict[y][x]
            c -= 1
        d += 1
    return ndict

def vflip(zdict):
    ndict = deepcopy(zdict)
    l = len(zdict)
    if l == 2:
        ndict[0] = zdict[1]
        ndict[1] = zdict[0]
    if l == 3:
        ndict[0] = zdict[2]
        ndict[2] = zdict[0]
    return ndict

def hflip(zdict):
    ndict = deepcopy(zdict)
    l = len(zdict[0])
    for y in zdict:
        if l == 2:
            ndict[y][0] = zdict[y][1]
            ndict[y][1] = zdict[y][0]
        if l == 3:
            ndict[y][0] = zdict[y][2]
            ndict[y][2] = zdict[y][0]
    return ndict

def matcher(xtup):
    xdict = xtup[1]
    xlen = len(xdict[0])
    tdict = deepcopy(xdict)
    
    for s in pro:
        if s == "r":
            tdict = rotater(xdict)
            xdict = deepcopy(tdict)
        if s == "h":
            tdict = hflip(xdict)
        if s == "v":
            tdict = vflip(xdict)

        sm = joinery(tdict)
        if sm in rules[xlen]:
            return (xtup[0], rules[xlen][sm])
    input("No match, break out")

if rank == 0:
    rules = {}
    rules[2] = {}
    rules[3] = {}

    with open("input21.txt") as fp:
        for line in fp:
            line = line.strip()
            chunk = line.split("/")
            rulep = line.split(" => ")
            rules[len(chunk[0])][rulep[0]] = rulep[1]
else:
    rules = None

rules = comm.bcast(rules, 0)
#print(rules)

# set input and number of iterations; part a: 5, part b: 18
inp = ".#./..#/###"
itr = 18

for i in range(0, itr):
    if rank == 0:
        fparts = inp.split("/")

        plist = []
        psize = 0
        if len(fparts[0]) % 2 == 0:
            fsize = len(fparts[0]) // 2
            fpos = 0
            for y in range(0, fsize):
                for x in range(0, fsize):
                    pdict = {}
                    for r in range(0,2):
                        pdict[r] = {}
                        pdict[r][0] = fparts[y*2+r][x*2]
                        pdict[r][1] = fparts[y*2+r][x*2+1]

                    plist.append((fpos, pdict))
                    fpos += 1

        elif len(fparts[0]) % 3 == 0:
            fsize = len(fparts[0]) // 3
            fpos = 0
            for y in range(0, fsize):
                for x in range(0, fsize):
                    pdict = {}
                    for r in range(0,3):
                        pdict[r] = {}
                        pdict[r][0] = fparts[y*3+r][x*3]
                        pdict[r][1] = fparts[y*3+r][x*3+1]
                        pdict[r][2] = fparts[y*3+r][x*3+2]

                    plist.append((fpos, pdict))
                    fpos += 1

        else:
            print("Anomalous behavior.")
            print(len(fparts))
            input()
        
        while len(plist) < size:
            plist.append((-1, ""))
        plist = np.array_split(plist, size)
    else:
        plist = None
    
    splist = comm.scatter(plist, 0)

    # broken up into blocks, now to split to the threads and rotate and compare
    nparts = {}
    #print(splist)
    for e in splist:
        if e[0] > -1:
            ntup = matcher(e)
            nparts[ntup[0]] = ntup[1]

    nparts = comm.gather(nparts, 0)
    
    if rank == 0:
        # merge the bloody dicts
        pdict = nparts[0]
        for x in range(1, len(nparts)):
            pdict.update(nparts[x])

        # build the new input
        # cols to build
        col = int(sqrt(len(pdict)))
        newinp = ""
        rpp = pdict[0].count("/")+1
        for o in range(0, col):
            for n in range(0, rpp):
                for m in range(0,col):
                    b = pdict[o*col+m].split("/")
                    newinp += b[n]
                newinp += "/"
        inp = newinp[:-1]

if rank == 0:
    fsum = 0
    for f in inp:
        fsum += f.count("#")
    print("Number of pixels on after", itr, "iterations:> ", fsum)