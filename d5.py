
jumps = []

with open("input5.txt") as fp:
    for line in fp:
        e = int(line.strip())
        jumps.append(e)

pos = 0
steps = 0
while pos < len(jumps):
    npos = pos + jumps[pos]
    # part2
    if jumps[pos] >= 3:
        jumps[pos] -= 1
    else:
        jumps[pos] += 1
    # part1
    #jumps[pos] += 1
    steps += 1
    pos = npos
    #print(jumps)
    #input()

print("Steps out: ", steps)