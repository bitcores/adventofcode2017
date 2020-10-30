
ops = []
prog = {}
sndstack = {}

with open("input23.txt") as fp:
    for line in fp:
        ops.append(line.strip())

    
class opcomp():

    def __init__(self, debug):
        self.reg = {}
        self.reg['a'] = debug
        self.pos = 0
        self.cycle = 0
        self.mode = 1
        self.mulcnt = 0

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
            return self.reg[self.chkreg(v)]

    # basic prime calc function
    def isPrime(self, n):
        for cn in range(2, n//2):
            if n % cn == 0:
                return False
        return True

    def runoc(self):

        while self.pos >= 0 and self.pos < len(ops):

            inp = ops[self.pos].split(" ")

            if self.pos == 11 and self.reg["a"] == 1:
                if not self.isPrime(self.reg["b"]):
                    self.reg["f"] = 0
                self.reg["d"] = self.reg["b"]
                self.reg["e"] = self.reg["e"]
                self.reg["g"] = 0
                self.pos = 24
                continue

            elif inp[0] == "set":
                a = self.chkreg(inp[1])
                b = self.chkinp(inp[2])
                self.reg[a] = b
            
            elif inp[0] == "sub":
                a = self.chkreg(inp[1])
                b = self.chkinp(inp[2])
                self.reg[a] -= b
            
            elif inp[0] == "mul":
                a = self.chkreg(inp[1])
                b = self.chkinp(inp[2])
                self.reg[a] = self.reg[a] * b
                self.mulcnt += 1
                
            elif inp[0] == "jnz":
                a = self.chkinp(inp[1])
                b = self.chkinp(inp[2])
                if a != 0:
                    self.pos = self.pos + b
                    self.cycle += 1
                    continue
            
            else:
                print("Instruction not found: ", inp[0])
                input()

            self.pos += 1
            self.cycle += 1

        self.mode = 0
        print("Program has terminated.")


p0 = opcomp(1)
p0.runoc()
print("mul was invoked", p0.mulcnt, "times.")
print("Value of register 'h' is", p0.reg[p0.chkreg('h')])
#print(p0.reg)
