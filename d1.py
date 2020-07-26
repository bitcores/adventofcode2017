
with open("input1.txt") as fp:
    for line in fp:
        csum = 0
        line = line.strip()
        llen = len(line)
        hlen = llen // 2
        for x in range(0, llen):
            #part 1
            y = x+1
            #part 2
            #y = x+hlen
            if y >= llen:
                y -= llen
            if line[x] == line[y]:
                csum += int(line[x])
        #print(line, csum)
        print("Captcha: ", csum)

