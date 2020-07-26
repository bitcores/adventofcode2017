reg = {}
instru = []

def initReg(r):
    if not r in reg:
        reg[r] = 0
    return r

def runCon(g, h, c):
    if c == "==":
        return g == h
    if c == ">":
        return g > h
    if c == "<":
        return g < h
    if c == ">=":
        return g >= h
    if c == "<=":
        return g <= h
    if c == "!=":
        return g != h
    print("condition failed")
    input()

with open("input8.txt") as fp:
    for line in fp:
        instru.append(line.strip())

ptr = 0
maxmem = 0

while ptr < len(instru):
    rd = instru[ptr]
    brk = rd.split(' ')
    # he doesnt use registers and ints in the same place in this problem
    # so checking if it is a reg or an int isn't required
    a = initReg(brk[0])
    b = initReg(brk[4])
    op = brk[1]
    x = int(brk[2])
    con = brk[5]
    y = int(brk[6])

    if op == 'cpy':
        t = brk[1]
        if t.isdigit():
            t = int(t)
        else:
            t = reg[t]
        reg[brk[2]] = t
    
    if op == 'inc':
        if runCon(reg[b], y, con):
            reg[a] = reg[a] + x

    if op == 'dec':
        if runCon(reg[b], y, con):
            reg[a] = reg[a] - x
    
    if brk[0] == 'jnz':
        t = brk[1]
        if t.isdigit():
            t = int(t)
        else:
            t = reg[t]
        if t != 0:
            ptr = ptr + int(brk[2])
        else:
            ptr += 1

    ptr += 1
    if max(reg.values()) > maxmem:
        maxmem = max(reg.values())

print("Max value in a reg at the end:", max(reg.values()))
print("Max value ever in a reg:", maxmem)