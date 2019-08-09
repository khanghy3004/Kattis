while 1:
	arr_a = []
	arr_b = []
	n = int(input())
	if n == -1:
		break
	for _ in range(n):
		a, b = map(int, input().split())
		arr_a.append(a)
		arr_b.append(b)
		sumN = 0
		sumN += arr_a[0] * arr_b[0]
		index = 0
		if len(arr_a) > 1:
			for i in range(1, len(arr_a)):
				sumN += arr_a[i] * (arr_b[i] - arr_b[index])
				index += 1
	print(sumN, 'miles')
