a = [int(x) for x in input().split()]
while (a != [1, 2, 3, 4, 5]):
    for i in range(4):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
            print(" ".join([str(x) for x in a]))
