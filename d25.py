
sstate = ""
diag = 0

statedict = {}
cstate = ""
cv = 0

with open("input25.txt") as fp:
    for line in fp:
        line = line.strip()
        
        if "Begin" in line:
            sstate = line[-2]
        elif "diagnostic" in line:
            diag = int(line.split(" ")[-2])
        elif "In state" in line:
            cstate = line[-2]
            statedict[cstate] = {}
        elif "current value" in line:
            cv = int(line[-2])
            statedict[cstate][cv] = {}
        elif "Write" in line:
            statedict[cstate][cv]["w"] = int(line[-2])
        elif "Move" in line:
            if "left" in line:
                statedict[cstate][cv]["m"] = -1
            else:
                statedict[cstate][cv]["m"] = 1
        elif "Continue" in line:
            statedict[cstate][cv]["s"] = line[-2]

#print(statedict)

tape = {}
cpos = 0
for e in range(0, diag):
    if not cpos in tape:
        tape[cpos] = 0
  
    npos = cpos + statedict[sstate][tape[cpos]]['m']
    nstate = statedict[sstate][tape[cpos]]['s']
    tape[cpos] = statedict[sstate][tape[cpos]]['w']
    cpos = npos
    sstate = nstate

nstr = 0
for x in tape:
    if tape[x] == 1:
        nstr += 1
print("Diagnostic checksum:> ", nstr)