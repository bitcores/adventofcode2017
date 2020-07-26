from copy import deepcopy

def strify(lst):
    rstr = ""
    for x in range(0,len(lst)):
        rstr += str(lst[x])
        if x < len(lst)-1:
            rstr += ","
    return rstr

with open("input6.txt") as fp:
    for line in fp:
        line = line.strip()
        banks = line.split("\t")

        for x in range(0,len(banks)):
            banks[x] = int(banks[x])
        
        bankset = []
        loopstr = ""
        bankset.append(strify(banks))
        cycles = 0

        while True:
            bigbank = 0
            maxbank = 0
            for x in range(0,len(banks)):
                if banks[x] > maxbank:
                    maxbank = banks[x]
                    bigbank = x
            
            tempbank = deepcopy(banks)
            tval = tempbank[bigbank]
            tempbank[bigbank] = 0
            p = bigbank
            while tval > 0:
                p = p+1
                if p >= len(banks):
                    p = 0
                tempbank[p] += 1
                tval -= 1

            cycles += 1
            tmpbstr = strify(tempbank)
            if tmpbstr in bankset:
                loopstr = tmpbstr
                break
            bankset.append(tmpbstr)
            banks = deepcopy(tempbank)
            
            #print(banks)
            #input()
        print("Cycles until loop detected: ", cycles)
        for x in range(0,len(bankset)):
            if bankset[x] == loopstr:
                loopset = bankset[x:]
                break
        print("Size of loop: ", len(loopset))