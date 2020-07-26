from itertools import permutations

okpass = 0

with open("input4.txt") as fp:
    for line in fp:
        wcset = set()
        fail = False
        words = line.strip().split(" ")
        for e in words:
            if e in wcset:
                break
            #part 2
            perms = list(permutations(e))
            for p in perms:
                if "".join(p) in wcset:
                    fail = True
                    break
            #/part2
            if not fail:
                wcset.add(e)
            
        if len(wcset) == len(words):
            okpass += 1

print("Valid No.: ", okpass)