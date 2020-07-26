
stack = ["#"]

#r = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
#r = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
#r = '<{o"i!a,<{i<a>'
f = open("input9.txt")
r = f.readline()
f.close()

score = 0
garbage = 0

skip = False
for x in r:
    if skip:
        skip = not skip
        continue
    if x == "!":
        skip = True
        continue
    if x == "<":
        if stack[-1] != "<":
            stack.append("<")
            continue
    if x == ">":
        if stack[-1] == "<":
            stack.pop(-1)
            continue
    if stack[-1] == "<":
        garbage += 1
        continue
    if x == "{":
        stack.append("{")
    if x == "}":
        stack.pop(-1)
        score += len(stack)

print("Group score:", score)
print("Garbage:", garbage)