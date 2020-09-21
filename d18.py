
ops = []
prog = {}
sndstack = {}

with open("input18.txt") as fp:
    for line in fp:
        ops.append(line.strip())

    
class opcomp():

    def __init__(self, p, partner):
        self.reg = {}
        self.lsf = 0  
        self.pos = 0
        self.cycle = 0
        self.mode = 1
        self.id = p
        self.partner = partner
        self.rcvcnt = 0
        self.fr = True
        sndstack[p] = []
        self.reg['p'] = self.id

    def isInt(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

    def chkreg(self, r):
        if r not in self.reg:
            self.reg[r] = 0
        return r

    def chkinp(self, v):
        if self.isInt(v):
            return int(v)
        else:
            return self.reg[v]

    def runoc(self):

        while self.pos >= 0 and self.pos < len(ops):

            inp = ops[self.pos].split(" ")

            if inp[0] == "snd":
                hz = self.chkinp(inp[1])
                sndstack[self.id].append(hz)
                #print("Play sound at", hz, "Hz")
            
            if inp[0] == "set":
                a = self.chkreg(inp[1])
                b = self.chkinp(inp[2])
                self.reg[a] = b

            if inp[0] == "add":
                a = self.chkreg(inp[1])
                b = self.chkinp(inp[2])
                self.reg[a] += b
            
            if inp[0] == "mul":
                a = self.chkreg(inp[1])
                b = self.chkinp(inp[2])
                self.reg[a] = self.reg[a] * b

            if inp[0] == "mod":
                a = self.chkreg(inp[1])
                b = self.chkinp(inp[2])
                self.reg[a] = self.reg[a] % b

            if inp[0] == "rcv":
                a = self.chkreg(inp[1])
                # Part 1
                if a != 0 and self.id == 0 and self.fr:
                    print("Recovered frequency:> ",sndstack[self.id][-1], "Hz")
                    self.fr = False
                ########

                if len(sndstack[self.partner]) > self.rcvcnt:
                    self.mode = 1 
                    self.reg[a] = sndstack[self.partner][self.rcvcnt]
                    self.rcvcnt += 1
                else:
                    self.mode = 99
                    return
                
            
            if inp[0] == "jgz":
                a = self.chkinp(inp[1])
                b = self.chkinp(inp[2])
                if a > 0:
                    self.pos = self.pos + b
                    self.cycle += 1
                    continue

            self.pos += 1
            self.cycle += 1

        self.mode = 0
        print("Program", self.id ,"has terminated.")


p0 = opcomp(0,1)
p1 = opcomp(1,0) 

deadlock = False
deadlocktest = False
lastcycle = {0: 0, 1: 0}
lockcnt = 0

while deadlock != True:
    if p0.mode != 0:
        p0.runoc()
    if p1.mode != 0:
        p1.runoc()

    if p0.cycle == lastcycle[0] and p1.cycle == lastcycle[1]:
        lockcnt += 1
        
        if lockcnt > 10:
            break
    else:
        lockcnt = 0

    lastcycle[0] = p0.cycle
    lastcycle[1] = p1.cycle
        
print("No. values sent by Program 1:> ", len(sndstack[1]))