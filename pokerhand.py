a = []
b = []
c = []
d = []
e = []
arr = []
cnt = 0
maxN = 0
a, b, c, d, e = input().split()
arr.append(a[0])
arr.append(b[0])
arr.append(c[0])
arr.append(d[0])
arr.append(e[0])
for i in range(0,5):
	for j in range(i,5):
		if(arr[i] == arr[j]):
			cnt += 1
	maxN = max(maxN, cnt)
	cnt = 0
print(maxN)