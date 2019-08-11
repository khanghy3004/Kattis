n = int(input())
for i in range(n):
	g = int(input())
	a = input().split()
	for x in a:
		if a.count(x) == 1:
			print("Case #%d: %d" % (i+1, int(x)))
			break