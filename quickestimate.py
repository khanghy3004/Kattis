n = int(input())
for _ in range(n):
	cost = int(input())
	ans = 0
	while cost > 0:
		cost = int(cost) / 10
		ans += 1
	if ans == 0:
		print(1)
	else:
		print(ans-1)