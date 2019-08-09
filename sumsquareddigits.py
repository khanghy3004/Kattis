p = int(input())
k = 0
b = 0
n = 0
for i in range(p):
	sumN = 0
	k, b, n = map(int, input().split())
	while n > 0:
		sumN += int((n % b)) * int((n % b))
		n /= b
	print(k, int(sumN))
	