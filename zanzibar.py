n = int(input())
for _ in range(n):
	ans = 0
	pre = 1
	for i in [int(x) for x in input().split()]:
		if (i > 2*pre):
			ans += i - (2*pre)
		pre = i	
	print(ans)
