n = int(input())
dec = 0
a = []
cnt = -1
while n > 0:
	cnt += 1
	a.append(int(n) % 2)
	n = int(n) / 2
for i in range(len(a)):
	cnt -= 1
	dec += a[i] * pow(2, cnt)
print(int(dec))