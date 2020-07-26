
#part 1
inp = 277678
r = 1
m = 1
c = 0

while r + m < inp:
    r += m
    m += 8
    c += 1

x = inp - r
y = x / c
z = x % c

print(c+z)

#part 2
def chkpos(y,x):
    if y in rdict:
        if x in rdict[y]:
            return rdict[y][x]
    return 0

def setval(y,x,val):
    global rdict
    if not y in rdict:
        rdict[y] = {}
    rdict[y][x] = val
    return

#y,x
#0,0 = 1
#d = 0 = y+1, 1 = x-1, 2 = y-1, 3 = x+1
rdict = {0:{0: 1 }}
r = 0
s = 1
t = 0
p = [0,1]
while r < inp:
    d = 0
    # the number of cells in loop is 8x(no. of loops from the center)
    nc = 8*s
    ns = nc // 4

    for g in range(0,5):
        if g == 4 and t == 0:
            # fifth unnecessary on first run
            continue
        if d > 3:
            d = 0
        adjns = ns
        if g == 0:
            adjns = ns - t
        if g == 3:
            adjns += 1
        if g == 4:
            adjns = t
        #print(adjns)
        for c in range(0,adjns):
            csum = 0
            # csum will be the sum of these existing positions
            if d == 0:
                # check y-1, x-1, x-1y+1, x-1y-1
                csum += chkpos(p[0]-1,p[1])                  
                csum += chkpos(p[0],p[1]-1)
                csum += chkpos(p[0]+1,p[1]-1)
                csum += chkpos(p[0]-1,p[1]-1)

                setval(p[0],p[1],csum)
                if c < adjns-1 or g == 4:
                    p[0] += 1
                else:
                    p[1] -= 1
            if d == 1:
                # check x+1, y-1, x-1y-1, x+1y-1
                csum += chkpos(p[0],p[1]+1)                  
                csum += chkpos(p[0]-1,p[1])
                csum += chkpos(p[0]-1,p[1]-1)
                csum += chkpos(p[0]-1,p[1]+1)

                setval(p[0],p[1],csum)
                if c < adjns-1:
                    p[1] -= 1
                else:
                    p[0] -= 1
            if d == 2:
                # check y+1, x+1, x+1y+1, x+1y-1
                csum += chkpos(p[0]+1,p[1])                  
                csum += chkpos(p[0],p[1]+1)
                csum += chkpos(p[0]+1,p[1]+1)
                csum += chkpos(p[0]-1,p[1]+1)

                setval(p[0],p[1],csum)
                if c < adjns-1:
                    p[0] -= 1
                else:
                    p[1] += 1
            if d == 3:
                # check x-1, y+1, x-1y+1, x+1y+1
                csum += chkpos(p[0],p[1]-1)                  
                csum += chkpos(p[0]+1,p[1])
                csum += chkpos(p[0]+1,p[1]-1)
                csum += chkpos(p[0]+1,p[1]+1)

                setval(p[0],p[1],csum)
                if c < adjns-1:
                    p[1] += 1
                else:
                    p[0] += 1

            if csum > r:
                r = csum
            if r > inp:
                break
            print(rdict)
            input()
        if r > inp:
            break
        d += 1

    s += 1
    t += 1

print(r)
print(rdict)