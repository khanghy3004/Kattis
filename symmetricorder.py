n = None
a = []
b = []
c = []
index = 0
while 1:
	index += 1
	n = int(input())
	if n == 0:
		break
	for i in range(0, n):
		a.append(input())
	print("SET ", index)
	for i in range(0, n):
		if i%2 == 0:
			b.append(a[i])
	for i in range(0, n):
		if i%2 == 1:
			c.append(a[i])
	for i in range(0, len(b)):
		print(b[i])
	for i in reversed(range(0, len(c))):
		print(c[i])
	a = []
	b = []
	c = []