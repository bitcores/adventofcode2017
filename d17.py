
#step = 3
step = 337
buf = [0]
pos = 0

# step 1, range 2018
# step 2, range 50000001

for x in range(1, 2018):
    pos = pos + step
    while pos > len(buf)-1:
        pos -= len(buf)
    
    #print(pos)
    if not pos == len(buf)-1:
        buf = buf[:pos+1] + [x] + buf[pos+1:]
        #print("split")
    else:
        buf.append(x)
        #print("append")

    pos += 1

    #print(buf)
    #input() 

print("Value after 2017:> ", buf[pos+1])

buf = [0,0]
pos = 0

for y in range (1, 50000001):
    pos = pos + step
    while pos > y-1:
        pos -= y
    
    #print(pos)
    if pos == 0:
        buf[1] = y

    pos += 1

    #print(buf)
    #input()

print("Value after 0:> ", buf[1])