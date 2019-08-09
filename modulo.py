cnt = 1
a = []

for _ in range(10):
	n = int(input())
	a.append(int(n) % 42)
a.sort()
k = a[0]
for i in range(1, len(a)):
	if k != a[i]:
		cnt += 1
		k = a[i]
print(cnt)