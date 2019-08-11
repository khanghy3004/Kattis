n = int(input())
a = sorted([int(input()) for i in range(n)], reverse=True)
total = 0
i = 0
while i + 2 < len(a):
	total += a[i] + a[i+1]
	i += 3
while i < len(a):
	total += a[i]
	i += 1
print(total)