n = int(input())
t = [int(x) for x in input().split()]
t.sort(reverse = True)
maxans = 0
for i in range(n):
	tmp = t[i] + i + 2
	maxans = max(maxans, tmp)
print(maxans)