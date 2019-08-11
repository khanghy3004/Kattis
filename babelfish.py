import sys
thisdict =  {}
s = input()
while s != "":
    x = s.split()  
    thisdict[x[1]] = x[0]
    s = input()

lines = sys.stdin.readlines()
for line in lines:
    if line[:-1] in thisdict:
        print(thisdict[line[:-1]])
    else:
        print("eh")