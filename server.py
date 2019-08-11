n, t = [int(x) for x in input().split()]
tasks = [int(x) for x in input().split()]
cnt_task = 0
ans = 0
for i in range(n):
	cnt_task += tasks[i]
	if cnt_task <= t:
		ans += 1
print(ans)
