def check(n, a, b):
	if n % (a + b) == 0 or n % (a + b) == a:
		return True
	return False
	
n = int(input())
avgN = int((n + 1) / 2)
print('{}:'.format(n))
for i in range(2, avgN + 1):
	for j in range(-1, 1):
		if check(n, i, i + j) == True:
			print('{},{}'.format(i, i + j))