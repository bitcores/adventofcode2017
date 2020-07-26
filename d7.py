
childrens = dict()
valuess = dict()
stringss = []

with open("input7.txt") as fp:
    for line in fp:
        line = line.strip()
        if "->" in line:
            parts = line.split(" -> ")
            string = parts[0]
            strval = string.split(" ")
            kids = parts[1].split(", ")
            valuess[strval[0]] = int(strval[1][1:-1])
            childrens[strval[0]] = dict()
            childrens[strval[0]]["parent"] = ""
            childrens[strval[0]]["children"] = kids
            for x in kids:
                if x in childrens:
                    childrens[x]["parent"] = strval[0]
            for y in childrens:
                if strval[0] in childrens[y]["children"]:
                    childrens[strval[0]]["parent"] = y
            stringss.append(strval[0])
        else:
            string = line
            strval = string.split(" ")
            valuess[strval[0]] = int(strval[1][1:-1])
            stringss.append(strval[0])

#print(childrens)
#print(valuess)
#print(stringss)
base = ""
for y in childrens:
    if childrens[y]["parent"] == "":
        print("Tree base: ", y)
        base = y
        break

#part 2
def sumstack(ssum, branch):
    for z in childrens[branch]["children"]:
        ssum += valuess[z]
        if z in childrens:
            ssum = sumstack(ssum, z)
    return ssum

found = False
while not found:
    stacks = dict()
    for c in childrens[base]["children"]:
        if c in childrens:
            tsum = sumstack(valuess[c], c)
        else:
            tsum = valuess[c]
        if not tsum in stacks:
            stacks[tsum] = []
        stacks[tsum].append(c)
        #print("sum of ", c, tsum)
    print(stacks)
    if len(stacks) > 1:
        for x in stacks:
            #print(x)
            if len(stacks[x]) == 1:
                m = stacks[x][0]
                #print(valuess[m])
                base = m
    else:
        found = True
        print("found ", base)
        print(valuess[base])


