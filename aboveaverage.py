c = int(input())
for _ in range(c):
	arr = list(map(int, input().split()))
	n = arr[0]
	del arr[0]
	sm = sum(arr)
	avg = sm/n
	cnt = 0
	for i in range(len(arr)):
		if arr[i] > avg:
			cnt += 1
	res = (cnt/n)*100
	print('%.3f' %res, end='%\n')