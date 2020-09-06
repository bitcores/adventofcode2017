
#genA = 65
#genB = 8921
genA = 289
genB = 629

facA = 16807
facB = 48271

divi = 2147483647

pairs = 0

# something tells me there is a mathematical trick to this, but i have the dumb
#part 1
#for x in range(0, 40000000):
#    genA = genA * facA % divi
#    genB = genB * facB % divi
#
#    comA = bin(genA)[-16:]
#    comB = bin(genB)[-16:]
#
#    if comA == comB:
#        pairs += 1
#    #print(genA, genB)
#    #print(comA, comB)
#    #input()

#part 2
numA = []
numB = []
while len(numB) < 5000000: 
    genA = genA * facA % divi
    genB = genB * facB % divi

    if genA % 4 == 0:
        numA.append(genA)
    if genB % 8 == 0:
        numB.append(genB)

for y in range(0, len(numB)):
    comA = bin(numA[y])[-16:]
    comB = bin(numB[y])[-16:]

    if comA == comB:
        pairs += 1

print("Number of pairs:> ", pairs)