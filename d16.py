
dancemoves = []
proglist = []

outlist = []

#test 5, real 16
progs = 16

for x in range(0, progs):
    proglist.append(chr(97+x))

def iterer(plist):
    for m in dancemoves:
        if m[0] == "s":
            # for spins longer than the list
            spin = int(m[1:]) % progs
            plist = plist[(spin*-1):] + plist[:(spin*-1)]
            continue
        
        if m[0] == "x":
            pos = m[1:].split("/")
            tmp = plist[int(pos[0])]
            plist[int(pos[0])] = plist[int(pos[1])]
            plist[int(pos[1])] = tmp
            continue

        if m[0] == "p":
            sear = m[1:].split("/")
            #print(plist.index('b'))
            pos1 = plist.index(sear[0])
            pos2 = plist.index(sear[1])
            tmp = plist[pos1]
            plist[pos1] = plist[pos2]
            plist[pos2] = tmp
            continue
        
        print("Error:> ", m)
        input()
    return plist


with open("input16.txt") as fp:
    for line in fp:
        indance = line.strip()
        dancemoves = indance.split(",")

        proglist = iterer(proglist)
        #print(dancemoves)
        #print(proglist)
        print("Program order:> ", ''.join(map(str, proglist)))

        for r in range(0, 1000000000):
            jp = ''.join(map(str, proglist))
            if jp in outlist:
                pos = outlist.index(jp)
                scale = r - pos
                rem = (1000000000 - pos) % scale
                # i wish there was an example result. when i found the loop but had the
                # wrong result i figured it was either +1 or -1
                inx = pos + rem - 1
                #print("Predicted index:> ", inx)
                proglist = outlist[inx]
                #print(outlist, len(outlist))
                input()
                break
            outlist.append(jp)
            proglist = iterer(proglist)
            #print(''.join(map(str, proglist)))
            #input()
        print("Order after 1bil:> ", ''.join(map(str, proglist)))
