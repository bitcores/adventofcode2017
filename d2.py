from copy import deepcopy
diffs = []

with open("input2.txt") as fp:
    for line in fp:
        low = 999999
        high = 0
        nums = line.split("\t")
        for x in nums:
            if int(x) < low:
                low = int(x)
            if int(x) > high:
                high = int(x)
        diffs.append(high - low)
#print(diffs)
print("Part 1: ", sum(diffs))

diffs2 = []

with open("input2.txt") as fp2:
    for line in fp2:
        nums = line.split("\t")
        for x in range(0, len(nums)):
            work = deepcopy(nums)
            work.pop(x)
            for y in work:
                if int(nums[x]) % int(y) == 0:
                    diffs2.append(int(nums[x]) // int(y))
                    break
print(diffs2)
print("Part 2: ", sum(diffs2))